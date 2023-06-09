# Generated by Django 4.1.4 on 2023-04-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuratMasuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kode', models.CharField(max_length=100)),
                ('Asal_surat', models.CharField(max_length=100)),
                ('Isi_Ringkasan', models.CharField(max_length=100)),
                ('File', models.FileField(upload_to='dokumen/')),
                ('Nomor', models.CharField(max_length=100)),
                ('Tanggal', models.DateField()),
                ('Pengirim', models.CharField(max_length=100)),
                ('Penerima', models.CharField(max_length=100)),
            ],
        ),
    ]
