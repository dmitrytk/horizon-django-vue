# Generated by Django 3.1.3 on 2020-11-26 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('type', models.CharField(blank=True, max_length=70, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'fields',
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('pad', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('alt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('bottom', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='api.field')),
            ],
            options={
                'db_table': 'wells',
                'unique_together': {('name', 'field')},
            },
        ),
    ]
