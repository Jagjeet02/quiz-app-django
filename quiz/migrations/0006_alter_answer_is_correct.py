# Generated by Django 5.1.4 on 2024-12-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_quizsession_correct_answers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
