# Generated by Django 5.0.1 on 2024-02-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                ("stock", models.IntegerField()),
                ("image_url", models.CharField(max_length=2083)),
            ],
        ),
    ]