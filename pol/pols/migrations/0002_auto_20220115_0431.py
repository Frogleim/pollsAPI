# Generated by Django 2.2 on 2022-01-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='answer_type',
            field=models.CharField(choices=[('1', 'Multiple'), ('2', 'Text'), ('3', 'Single')], default=1, max_length=30),
        ),
        migrations.AlterField(
            model_name='choice',
            name='answer_choices',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=1, max_length=10),
        ),
    ]