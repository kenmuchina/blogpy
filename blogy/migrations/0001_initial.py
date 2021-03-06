# Generated by Django 3.1.7 on 2021-03-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('secondname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('field', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogy.author')),
            ],
        ),
    ]
