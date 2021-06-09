# Generated by Django 3.2.4 on 2021-06-08 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('owner', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=250)),
                ('event_text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('event_date', models.DateTimeField(verbose_name='date event')),
            ],
        ),
    ]