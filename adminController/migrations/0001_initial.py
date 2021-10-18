# Generated by Django 3.1.7 on 2021-10-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
            ],
        ),
    ]