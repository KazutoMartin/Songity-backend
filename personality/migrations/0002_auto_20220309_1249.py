# Generated by Django 3.1.6 on 2022-03-09 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personality',
            name='energy',
            field=models.CharField(choices=[('N', 'INTUITIVE'), ('S', 'OBSERVANT')], max_length=1, verbose_name='Energy'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='energy_p',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Energy percentage'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='mind',
            field=models.CharField(choices=[('E', 'EXTRAVERTED'), ('I', 'INTROVERTED')], max_length=1, verbose_name='Mind'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='mind_p',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Mind percentage'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='nature',
            field=models.CharField(choices=[('F', 'FEELING'), ('T', 'THINKING')], max_length=1, verbose_name='Nature'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='nature_p',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Nature percentage'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='tactics',
            field=models.CharField(choices=[('J', 'JUDGING'), ('P', 'Email')], max_length=1, verbose_name='Tactics'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='tactics_p',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Tactics percentage'),
        ),
    ]
