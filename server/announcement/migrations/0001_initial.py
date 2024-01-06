# Generated by Django 4.2.7 on 2024-01-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'ordering': ('-time',),
                'permissions': [('full', '管理公告')],
                'default_permissions': (),
            },
        ),
    ]
