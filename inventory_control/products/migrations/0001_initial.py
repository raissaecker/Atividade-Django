# Generated by Django 5.0.1 on 2024-01-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('slug', models.SlugField(unique=True)),
                ('is_perishable', models.BooleanField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products')),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails')),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]