# Generated by Django 3.0.3 on 2023-02-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('question', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.TextField(blank=True, null=True, verbose_name='Your answer')),
                ('cmd_msg', models.TextField(blank=True, null=True, verbose_name='输出结果')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='Practise')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Program', verbose_name='Programming')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Programming Questions Answer Record',
                'verbose_name_plural': 'Programming Questions Answer Record',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='JudgeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.TextField(blank=True, null=True, verbose_name='Your answer')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Judge', verbose_name='True or False')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='Practise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Judgment question answer record',
                'verbose_name_plural': 'Judgment question answer record',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FillRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.TextField(blank=True, null=True, verbose_name='Your answer')),
                ('fill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Fill', verbose_name='Blank')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='Practise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Fill in the blank questions and answer records',
                'verbose_name_plural': 'Fill in the blank questions and answer records',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.TextField(blank=True, null=True, verbose_name='Your answer')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Choice', verbose_name='Choice')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='Practise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Selected Questions Answer Record',
                'verbose_name_plural': 'Selected Questions Answer Record',
                'ordering': ['id'],
            },
        ),
    ]
