# Generated by Django 4.0.8 on 2023-11-06 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_remove_ads_image_adsimage_ads_alter_adsimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adsimage',
            name='ads',
        ),
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ads.adsimage'),
            preserve_default=False,
        ),
    ]