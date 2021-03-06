# Generated by Django 3.1.6 on 2022-01-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220104_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='google_profile_url',
            field=models.URLField(blank=True, null=True, verbose_name='Google Profile URL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='google_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='Google ID'),
        ),
    ]
