# Generated by Django 3.0.3 on 2020-04-21 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_exercise_recode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['id'], 'verbose_name': '练习', 'verbose_name_plural': '练习'},
        ),
        migrations.AlterModelOptions(
            name='recode',
            options={'ordering': ['id'], 'verbose_name': '练习记录', 'verbose_name_plural': '练习记录'},
        ),
        migrations.AddField(
            model_name='exercise',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 21, 23, 22, 51, 717049), verbose_name='练习时间'),
            preserve_default=False,
        ),
    ]
