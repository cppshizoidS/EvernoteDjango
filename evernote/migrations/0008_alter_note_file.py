# Generated by Django 4.0 on 2022-06-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evernote', '0007_alter_note_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='notes_files/'),
        ),
    ]
