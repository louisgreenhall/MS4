from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('draw_type', models.CharField(default='', max_length=255)),
                ('colour', models.CharField(default='', max_length=255)),
                ('backing', models.CharField(default='', max_length=255)),
                ('files', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
