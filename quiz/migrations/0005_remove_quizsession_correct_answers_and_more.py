# Generated by Django 5.1.4 on 2024-12-18 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizsession',
            name='correct_answers',
        ),
        migrations.RemoveField(
            model_name='quizsession',
            name='incorrect_answers',
        ),
        migrations.RemoveField(
            model_name='quizsession',
            name='total_questions',
        ),
        migrations.AddField(
            model_name='quizsession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-12-19 00:00:46'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizsession'),
        ),
    ]