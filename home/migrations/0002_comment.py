# Generated by Django 3.1.4 on 2020-12-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.TextField()),
                ('request_id', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
