# Generated by Django 2.2.26 on 2022-03-13 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_id', models.IntegerField(unique=True)),
                ('gallery_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_id', models.IntegerField(unique=True)),
                ('piece_name', models.CharField(max_length=50)),
                ('gallery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyParty.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('user_name', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(unique=True)),
                ('rating', models.IntegerField()),
                ('piece_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyParty.Piece')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyParty.User')),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyParty.User'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyParty.User'),
        ),
    ]