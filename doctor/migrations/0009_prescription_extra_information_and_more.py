# Generated by Django 4.0.6 on 2022-09-09 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_admin', '0001_initial'),
        ('doctor', '0008_doctor_information_nid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='extra_information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital_admin.hospital_department'),
        ),
        migrations.AlterField(
            model_name='doctor_information',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital_admin.specialization'),
        ),
    ]
