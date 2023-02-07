# Generated by Django 4.1.6 on 2023-02-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question", "0003_auto_20230206_1529"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="answer_A",
            field=models.CharField(default="", max_length=256, verbose_name="Option A"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="answer_B",
            field=models.CharField(default="", max_length=256, verbose_name="Option B"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="answer_C",
            field=models.CharField(default="", max_length=256, verbose_name="Option C"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="answer_D",
            field=models.CharField(default="", max_length=256, verbose_name="Option D"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="answer_E",
            field=models.CharField(
                blank=True, default="", max_length=256, verbose_name="Option E"
            ),
        ),
        migrations.AlterField(
            model_name="choice",
            name="answer_F",
            field=models.CharField(
                blank=True, default="", max_length=256, verbose_name="Option F"
            ),
        ),
    ]