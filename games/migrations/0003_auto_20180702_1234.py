# Generated by Django 2.0.6 on 2018-07-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('weight', models.FloatField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]