# Generated by Django 3.1.1 on 2020-10-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200910_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Federation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Federation', models.CharField(choices=[('Martial arts', 'Martial arts   '), ('Full contact sports', 'Full contact sports'), ('MMA', 'MMA'), ('Karate', 'Karate'), ('Applied arts', 'Applied arts')], max_length=20)),
            ],
        ),
    ]
