# Generated by Django 4.1 on 2024-02-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]