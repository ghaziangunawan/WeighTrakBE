# Generated by Django 4.1 on 2025-01-30 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('body_fat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('times_worked_this_week', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOut',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('S', 'Strength'), ('C', 'Cardio')], max_length=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOutSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('duration', models.DurationField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.session')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.workout')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOutMuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.musclegroup')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.workout')),
            ],
        ),
    ]
