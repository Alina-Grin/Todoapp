# Generated by Django 2.1.5 on 2019-02-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190213_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создана'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.CharField(max_length=64, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]