# Generated by Django 4.2.7 on 2023-11-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание о нас')),
            ],
            options={
                'verbose_name': ('О нас',),
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='history_image_1', verbose_name='Первая фотография')),
                ('image_2', models.ImageField(upload_to='history_image_2', verbose_name='Второя фотография')),
                ('descriptions', models.TextField(verbose_name='Описание истории')),
            ],
            options={
                'verbose_name': ('Наша история',),
                'verbose_name_plural': 'Наша история',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='offer_image', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('descriptions', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('type', models.CharField(max_length=255, verbose_name='Тип блюда')),
            ],
            options={
                'verbose_name': ('Предложение',),
                'verbose_name_plural': 'Предложение',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image', verbose_name='Фотография для слайда')),
                ('title', models.CharField(max_length=255, verbose_name='Название для слайда')),
                ('descriptions', models.TextField(verbose_name='Описание для слайда')),
            ],
            options={
                'verbose_name': ('Слайд',),
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': ('Основные параметры',), 'verbose_name_plural': 'Основные параметры'},
        ),
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Facebook'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Instagram'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(upload_to='logo_image', verbose_name='Логотоип сайта'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Телейонный номер'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Youtube'),
        ),
    ]