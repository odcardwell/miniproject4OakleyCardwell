# Generated by Django 5.1.2 on 2024-11-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='About Me', max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]