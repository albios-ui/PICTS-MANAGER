# Generated by Django 4.1.7 on 2023-03-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='albumacces',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photoaccess',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]