from django.db import models

class COGUK_BiosourceSamplingProcessSupplement(models.Model):
    sampling = models.OneToOneField('BiosourceSamplingProcess', on_delete=models.CASCADE, related_name="coguk_supp")
    is_surveillance = models.BooleanField(null=True)
    is_hcw = models.BooleanField(null=True)
    employing_hospital_name = models.CharField(max_length=100, blank=True, null=True)
    employing_hospital_trust_or_board = models.CharField(max_length=100, blank=True, null=True)
    is_hospital_patient = models.BooleanField(null=True)
    is_icu_patient = models.BooleanField(null=True)
    admission_date = models.DateField(blank=True, null=True)
    admitted_hospital_name = models.CharField(max_length=100, blank=True, null=True)
    admitted_hospital_trust_or_board = models.CharField(max_length=100, blank=True, null=True)
    is_care_home_worker = models.BooleanField(null=True)
    is_care_home_resident = models.BooleanField(null=True)
    anonymised_care_home_code = models.CharField(max_length=10, blank=True, null=True)
    admitted_with_covid_diagnosis = models.BooleanField(null=True)
    collection_pillar = models.PositiveSmallIntegerField(blank=True, null=True)

    def get_resty_serializer(self):
        from . import resty_serializers
        return resty_serializers.RestyCOGUK_BiosourceSamplingProcessSupplement
