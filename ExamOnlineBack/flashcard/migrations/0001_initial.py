# Generated by Django 4.1.6 on 2023-02-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("front", models.TextField()),
                ("back", models.TextField()),
                ("image", models.URLField(blank=True, null=True)),
                ("video_link", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "flash card",
                "db_table": "card",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Deck",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("image", models.URLField(blank=True, null=True)),
                ("description", models.TextField()),
                ("cards", models.ManyToManyField(to="flashcard.card")),
            ],
            options={
                "verbose_name": "desk card",
                "db_table": "desk",
                "ordering": ["id"],
            },
        ),
    ]
