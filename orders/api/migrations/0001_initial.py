# Generated by Django 2.2.1 on 2019-05-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=100)),
                ('items', models.TextField(null=True)),
            ],
        ),
    ]