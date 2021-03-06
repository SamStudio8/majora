# Generated by Django 2.2.10 on 2020-04-25 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0061_auto_20200425_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='PAGQualityBasicTestDecision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='PAGQualityReportDecisionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pass', models.BooleanField(default=False)),
                ('is_warn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PAGQualityReportRuleRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_metric_str', models.CharField(blank=True, max_length=64, null=True)),
                ('is_pass', models.BooleanField(default=False)),
                ('is_warn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PAGQualityTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PAGQualityTestRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=64)),
                ('rule_desc', models.CharField(max_length=128)),
                ('metric_namespace', models.CharField(max_length=64)),
                ('metric_name', models.CharField(max_length=64)),
                ('warn_min', models.FloatField(blank=True, null=True)),
                ('warn_max', models.FloatField(blank=True, null=True)),
                ('fail_min', models.FloatField(blank=True, null=True)),
                ('fail_max', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PAGQualityTestVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveSmallIntegerField()),
                ('version_date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='versions', to='majora2.PAGQualityTest')),
            ],
        ),
        migrations.RemoveField(
            model_name='pagqualityreport',
            name='test_set_ruleset',
        ),
        migrations.RemoveField(
            model_name='pagqualityreportgroup',
            name='test_set_name',
        ),
        migrations.AddField(
            model_name='temporarymajoraartifactmetric',
            name='namespace',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='pagqualityreport',
            name='test_set_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reports', to='majora2.PAGQualityTestVersion'),
        ),
        migrations.DeleteModel(
            name='PAGQualityReportRecord',
        ),
        migrations.AddField(
            model_name='pagqualitytestrule',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rules', to='majora2.PAGQualityTestVersion'),
        ),
        migrations.AddField(
            model_name='pagqualityreportrulerecord',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tests', to='majora2.PAGQualityReport'),
        ),
        migrations.AddField(
            model_name='pagqualityreportrulerecord',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majora2.PAGQualityTestRule'),
        ),
        migrations.AddField(
            model_name='pagqualityreportdecisionrecord',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='decisions_as_a', to='majora2.PAGQualityReportRuleRecord'),
        ),
        migrations.AddField(
            model_name='pagqualityreportdecisionrecord',
            name='b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='decisions_as_b', to='majora2.PAGQualityReportRuleRecord'),
        ),
        migrations.AddField(
            model_name='pagqualityreportdecisionrecord',
            name='decision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majora2.PAGQualityBasicTestDecision'),
        ),
        migrations.AddField(
            model_name='pagqualityreportdecisionrecord',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='decisions', to='majora2.PAGQualityReport'),
        ),
        migrations.AddField(
            model_name='pagqualitybasictestdecision',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rules_as_a', to='majora2.PAGQualityTestRule'),
        ),
        migrations.AddField(
            model_name='pagqualitybasictestdecision',
            name='b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rules_as_b', to='majora2.PAGQualityTestRule'),
        ),
        migrations.AddField(
            model_name='pagqualitybasictestdecision',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='decisions', to='majora2.PAGQualityTestVersion'),
        ),
        migrations.AddField(
            model_name='pagqualityreportgroup',
            name='test_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='report_groups', to='majora2.PAGQualityTest'),
        ),
    ]
