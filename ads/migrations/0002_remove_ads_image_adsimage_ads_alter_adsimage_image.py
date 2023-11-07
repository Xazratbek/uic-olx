# Generated by Django 4.0.8 on 2023-11-06 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='image',
        ),
        migrations.AddField(
            model_name='adsimage',
            name='ads',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='ads.ads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adsimage',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='ads_images'),
        ),
    ]