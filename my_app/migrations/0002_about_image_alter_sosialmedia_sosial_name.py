# Generated by Django 4.2.5 on 2023-12-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='sosialmedia',
            name='sosial_name',
            field=models.CharField(choices=[('insta', 'Instagram'), ('fb', 'Facebook'), ('wp', 'WhatsApp'), ('twitter', 'Twitter'), ('linkedin', 'Linkedin'), ('tiktok', 'Tiktok'), ('github', 'GitHub')], max_length=255, verbose_name='sosial media hesabi'),
        ),
    ]