# Generated by Django 4.1.3 on 2022-12-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proyectofinal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccionUSA",
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
                ("empresa", models.CharField(max_length=100)),
                ("ticker", models.CharField(max_length=10)),
                ("precio", models.FloatField()),
            ],
        ),
    ]