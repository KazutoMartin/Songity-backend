# Generated by Django 3.1.6 on 2022-03-07 11:09

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mind', models.CharField(max_length=1, verbose_name='Mind')),
                ('mind_p', models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Mind percentage')),
                ('energy', models.CharField(max_length=1, verbose_name='Energy')),
                ('energy_p', models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Energy percentage')),
                ('nature', models.CharField(max_length=1, verbose_name='Nature')),
                ('nature_p', models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Nature percentage')),
                ('tactics', models.CharField(max_length=1, verbose_name='Tactics')),
                ('tactics_p', models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Tactics percentage')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
        ),
    ]
