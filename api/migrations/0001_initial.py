# Generated by Django 3.1.6 on 2023-04-21 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('job_type', models.CharField(choices=[('Full Time', 'fulltime'), ('Part Time', 'parttime'), ('Internship', 'intern'), ('Freelancer', 'freelancer')], max_length=200, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'others')], max_length=200, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('job_applied', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.application')),
            ],
        ),
    ]
