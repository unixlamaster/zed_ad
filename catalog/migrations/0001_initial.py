# Generated by Django 2.0.5 on 2018-06-23 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclature', models.CharField(max_length=50)),
                ('brend', models.CharField(max_length=50)),
                ('articul', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=2048)),
                ('catnumber', models.CharField(max_length=50)),
                ('oemnumber', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=1024)),
                ('urlprice', models.CharField(max_length=2048)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Provider'),
        ),
    ]
