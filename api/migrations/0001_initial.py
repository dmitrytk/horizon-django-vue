# Generated by Django 3.1.3 on 2020-12-07 11:07

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
                ('name', models.CharField(max_length=70)),
                ('pad', models.CharField(blank=True, max_length=70, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
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
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=30, null=True)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('dynamic_level', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('static_level', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.well')),
            ],
            options={
                'db_table': 'rates',
            },
        ),
        migrations.CreateModel(
            name='Inclinometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md', models.DecimalField(decimal_places=2, max_digits=20)),
                ('inc', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('azi', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inc', to='api.well')),
            ],
            options={
                'db_table': 'inclinometry',
            },
        ),
        migrations.CreateModel(
            name='FieldCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='api.field')),
            ],
            options={
                'db_table': 'field_coordinates',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('top_md', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('bot_md', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('top_tvd', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('bot_tvd', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('h', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.well')),
            ],
            options={
                'db_table': 'zones',
                'unique_together': {('name', 'well')},
            },
        ),
        migrations.CreateModel(
            name='Mer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=30, null=True)),
                ('production', models.DecimalField(decimal_places=2, max_digits=30, null=True)),
                ('work_days', models.IntegerField(null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.well')),
            ],
            options={
                'db_table': 'mer',
                'unique_together': {('well', 'date')},
            },
        ),
    ]