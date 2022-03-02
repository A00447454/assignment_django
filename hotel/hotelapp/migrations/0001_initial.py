# Generated by Django 4.0.3 on 2022-03-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(null=True)),
            ],
        ),
    ]
