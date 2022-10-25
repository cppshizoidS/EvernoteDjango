# Generated by Django 4.0 on 2022-06-12 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evernote', '0004_alter_note_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='file',
        ),
        migrations.CreateModel(
            name='NoteFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.BinaryField(editable=True, null=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evernote.note')),
            ],
        ),
    ]
