from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_condition import Or

from two_factor.views.mixins import OTPRequiredMixin

from majora2 import tasks
from majora2 import models
from majora2 import resty_serializers as serializers
from majora2.authentication import TatlTokenAuthentication, APIKeyPermission
from tatl.models import TatlRequest, TatlPermFlex

import uuid
import json

# Honestly, this was so much fucking easier when it was my own code ffs
class MajoraDispatchMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.response_uuid = uuid.uuid4()
        start_ts = timezone.now()

        # Best effort grab source IP
        # https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
        remote_addr = None
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            remote_addr = x_forwarded_for.split(',')[0]
        else:
            remote_addr = request.META.get('REMOTE_ADDR')

        treq = TatlRequest(
            user = None,
            substitute_user = None,
            route = request.path,
            timestamp = start_ts,
            remote_addr = remote_addr,
            response_uuid = self.response_uuid,
        )
        treq.save()

        ret = super().dispatch(request, *args, **kwargs)
        return ret

    #def initial(request, *args, **kwargs):
    #    super().initial(request, *args, **kwargs)
    #    treq = TatlRequest.objects.get(response_uuid=self.response_uuid)
    #    treq.user = request.user
    #    treq.save()

    def finalize_response(self, request, response, *args, **kwargs):
        ret = super().finalize_response(request, response, *args, **kwargs)

        treq = TatlRequest.objects.get(response_uuid=self.response_uuid)
        treq.response_time = timezone.now() - treq.timestamp
        treq.payload = json.dumps(request.data)

        return ret

class RequiredParamRetrieveMixin(object):

    def _check_param(self, request):
        # Check the view has the required params (if any)
        for param in self.majora_required_params:
            if param not in request.query_params:
                return Response({"detail": "Your request is missing a required parameter: %s" % param}, HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        bad = self._check_param(request)
        if bad:
            return bad
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        bad = self._check_param(request)
        if bad:
            return bad
        return super().list(request, *args, **kwargs)

class MajoraCeleryListingMixin(object):
    def list(self, request, *args, **kwargs):
        queryset = list(self.filter_queryset(self.get_queryset()).values_list('id', flat=True))

        api_o = {}

        if self.celery_task:
            context = {}
            s_context = super().get_serializer_context()
            for param in self.majora_required_params:
                context[param] = request.query_params[param]
            celery_task = self.celery_task.delay(queryset, context=context, user=request.user.pk, response_uuid=self.response_uuid)
            if celery_task:
                api_o["response_uuid"] = self.response_uuid
                api_o["errors"] = 0
                api_o["test"] = request.query_params
                api_o["expected_n"] = len(queryset)
                api_o["tasks"] = celery_task.id
                api_o["messages"] = "Call api.majora.task.get with the appropriate task ID later..."
            else:
                api_o["errors"] = 1
                api_o["messages"] = "Could not add requested task to Celery..."
            return Response(
                api_o
            )


class MajoraUUID4orDiceNameLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}

        filter_on = "pk"
        if self.majora_alternative_field:
            # Try ID as UUID, else assume its a "dice_name" (majora internal name)
            if type(self.kwargs["pk"]) != uuid.UUID:
                try:
                    # Check if this parameter looks like a UUID anyway
                    uuid.UUID(self.kwargs["pk"], version=4)
                except ValueError:
                    filter_on = self.majora_alternative_field

        filter[filter_on] = self.kwargs["pk"]
        obj = get_object_or_404(queryset, **filter) # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class ArtifactDetail(MajoraUUID4orDiceNameLookupMixin, generics.RetrieveAPIView):
    queryset = models.MajoraArtifact.objects.all()
    serializer_class = serializers.RestyArtifactSerializer
    majora_alternative_field = "dice_name"

class BiosampleView(
                    MajoraUUID4orDiceNameLookupMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.BiosampleArtifact.objects.all()
    serializer_class = serializers.RestyBiosampleArtifactSerializer
    majora_alternative_field = "dice_name"
    #TODO permissions class


class TaskView(APIView):
    #renderer_classes = [JSONRenderer]
    def get(self, request, tid, format=None):
        task_id = tid
        if not task_id:
            return Response({"booooooooooooo": 1})

        api_o = {}
        from mylims.celery import app
        res = app.AsyncResult(task_id)
        if res.state == "SUCCESS":
            try:
                api_o.update(res.get())
            except Exception as e:
                api_o["errors"] = 1
                api_o["messages"] = str(e)
        else:
            api_o["warnings"] = 1
            api_o["messages"] = "Task is not (yet) SUCCESS..."

        api_o["task"] = {
            "id": task_id,
            "state": res.state,
        }
        return Response(api_o)


#TODO How to handle errors properly here? Just let them 500 for now
class RestyDataview(
                    MajoraDispatchMixin,
                    #MajoraUUID4orDiceNameLookupMixin,
                    RequiredParamRetrieveMixin,
                    MajoraCeleryListingMixin,
                    viewsets.GenericViewSet):

    permission_classes = (APIKeyPermission,)

    celery_task = tasks.task_get_mdv_v3
    majora_api_permission = "majora2.can_read_dataview_via_api"
    majora_required_params = ["mdv"]

    def get_serializer_class(self):
        mdv_code = self.request.query_params.get("mdv")
        mdv = models.MajoraDataview.objects.get(code_name=mdv_code)

        from django.apps import apps
        return apps.get_model("majora2", mdv.entry_point).get_resty_serializer()

    def get_queryset(self):
        mdv_code = self.request.query_params.get("mdv")
        mdv = models.MajoraDataview.objects.get(code_name=mdv_code)

        from django.apps import apps
        model = apps.get_model("majora2", mdv.entry_point)
        return model.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        mdv = self.request.query_params.get("mdv")
        # I tried to raise http400 here but it didnt seem to work
        context.update({"mdv": mdv})
        return context

#TODO We'll start with PAG as the default entry point for Dataviews but in future
# we can probably move to specifying the entry point serializer and work from there
class PublishedArtifactGroupView(
                    MajoraUUID4orDiceNameLookupMixin,
                    RequiredParamRetrieveMixin,
                    MajoraCeleryListingMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = serializers.RestyPublishedArtifactGroupSerializer
    majora_alternative_field = "published_name"
    queryset = models.PublishedArtifactGroup.objects.all()

    celery_task = tasks.task_get_pag_by_qc_v3

    permission_classes = (Or(permissions.IsAuthenticated, APIKeyPermission),)
    majora_api_permission = "majora2.can_read_dataview_via_api"
    majora_required_params = ["mdv"]
    #renderer_classes = [JSONRenderer]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        mdv = self.request.query_params.get("mdv")
        # I tried to raise http400 here but it didnt seem to work
        context.update({"mdv": mdv})
        return context

    def get_queryset(self):
        queryset = self.queryset

        service = self.request.query_params.get('service', None)
        public = self.request.query_params.get('public', None)
        private = self.request.query_params.get('private', None)

        if public and private:
            # Ignore
            pass
        elif public:
            if service:
                queryset = queryset.filter(accessions__service=service)
            else:
                queryset = queryset.filter(is_public=True)
        elif private:
            if service:
                queryset = queryset.filter(~Q(accessions__service=service))
            else:
                queryset = queryset.filter(is_public=False)
        return queryset

