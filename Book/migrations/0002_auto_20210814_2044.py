# Generated by Django 3.2.5 on 2021-08-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
