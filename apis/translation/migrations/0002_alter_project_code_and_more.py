# Generated by Django 5.0.3 on 2024-03-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddConstraint(
            model_name='translate',
            constraint=models.UniqueConstraint(fields=('language', 'translation_key'), name='translate_unique_translation_key_per_language'),
        ),
        migrations.AddConstraint(
            model_name='translationkey',
            constraint=models.UniqueConstraint(fields=('key', 'project'), name='translate_key_unique_project'),
        ),
    ]
