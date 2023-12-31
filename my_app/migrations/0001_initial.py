# Generated by Django 5.0 on 2023-12-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ad')),
                ('surname', models.CharField(max_length=255, verbose_name='soyad')),
                ('adress', models.CharField(max_length=255, verbose_name='adress')),
                ('telephone', models.CharField(max_length=255, verbose_name='telefon')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(verbose_name='movzu')),
            ],
            options={
                'verbose_name': 'haqqinda',
                'verbose_name_plural': 'haqqinda',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='adi')),
                ('company_name', models.CharField(max_length=255, verbose_name='sert.ver. comp')),
                ('date_of', models.CharField(max_length=255, verbose_name='cert. ver. tarixi')),
            ],
            options={
                'verbose_name': 'sertifikatlar',
                'verbose_name_plural': 'sertifikatlar',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255, verbose_name='uni adi')),
                ('degree', models.CharField(max_length=255, verbose_name='derece')),
                ('profession', models.CharField(max_length=255, verbose_name='ixtisas')),
                ('education_years', models.CharField(max_length=255, verbose_name='tehsil muddeti')),
            ],
            options={
                'verbose_name': 'tehsil',
                'verbose_name_plural': 'tehsil',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='pesesi')),
                ('company_name', models.CharField(max_length=255, verbose_name='sirket adi')),
                ('description', models.TextField(verbose_name='movzu')),
                ('working_years', models.CharField(max_length=255, verbose_name='isleme vaxtlari')),
            ],
            options={
                'verbose_name': 'tecrube',
                'verbose_name_plural': 'tecrube',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='movzu')),
            ],
            options={
                'verbose_name': 'maraqlar',
                'verbose_name_plural': 'maraqlar',
            },
        ),
        migrations.CreateModel(
            name='SosialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sosial_name', models.CharField(choices=[('insta', 'Instagram'), ('fb', 'Facebook'), ('wp', 'WhatsApp'), ('twitter', 'Twitter'), ('linkedin', 'Linkedin'), ('tiktok', 'Tiktok')], max_length=255, verbose_name='sosial media hesabi')),
                ('sosial_link', models.TextField(verbose_name='sosial media linki')),
            ],
            options={
                'verbose_name': 'sosial media hesabi',
                'verbose_name_plural': 'sosial media hesablari',
                'ordering': ('sosial_name',),
            },
        ),
    ]
