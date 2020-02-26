# Generated by Django 2.2.3 on 2019-07-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hakkimizda', models.TextField(blank=True)),
                ('hakkimizdaimage', models.ImageField(upload_to='images')),
                ('iletisim', models.TextField(blank=True)),
                ('iletisimimage', models.ImageField(upload_to='images')),
                ('smtpserver', models.CharField(max_length=255)),
                ('smtpport', models.CharField(max_length=255)),
                ('smtpmail', models.CharField(max_length=255)),
                ('smtppass', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('pinterest', models.CharField(max_length=255)),
                ('gplus', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
                ('tumblr', models.CharField(max_length=255)),
                ('kisailetisim', models.TextField()),
                ('kisahakkimizda', models.TextField()),
                ('adres', models.CharField(max_length=255)),
                ('sehir', models.CharField(max_length=255)),
                ('fax', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]