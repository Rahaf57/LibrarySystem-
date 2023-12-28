# Generated by Django 3.2.23 on 2023-12-27 16:44

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('signatory', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=30, unique=True)),
                ('peges', models.IntegerField(max_length=11)),
                ('publication_year', models.IntegerField()),
                ('description', models.TextField()),
                ('edition', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('category_persion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Copies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='eBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('extension', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('content_persian', models.TextField()),
                ('privacy', models.TextField()),
                ('privacy_persian', models.TextField()),
                ('service', models.TextField()),
                ('service_persian', models.TextField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('publisher', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=100)),
                ('section_persion', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Book.category')),
            ],
        ),
    ]