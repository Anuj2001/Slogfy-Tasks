# Generated by Django 3.0.7 on 2020-09-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyTodo', '0002_auto_20200928_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Intermediate', 'Intermediate'), ('High', 'High')], max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Yet To Start', 'Yet To Start'), ('In Progess', 'In Progress'), ('In Review', 'In Review'), ('Completed', 'Completed')], max_length=100),
        ),
    ]
