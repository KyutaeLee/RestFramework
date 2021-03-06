# Generated by Django 2.0.3 on 2018-03-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, default=True, max_length=20)),
                ('pw', models.CharField(blank=True, default=True, max_length=12)),
                ('title', models.CharField(blank=True, default=True, max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
