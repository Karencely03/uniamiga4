# Generated by Django 3.1.7 on 2021-04-04 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UniamigaApp', '0006_remove_tutor_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('Descripcion', models.TextField(max_length=150)),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UniamigaApp.tutor')),
            ],
        ),
        migrations.DeleteModel(
            name='historia_clinica',
        ),
    ]