# Generated by Django 4.0.4 on 2022-05-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_job_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('dateofofferlettergenerated', models.DateField()),
                ('jobrole', models.CharField(max_length=300)),
                ('salary', models.CharField(max_length=300)),
                ('dateofjoining', models.DateField()),
                ('joblocation', models.CharField(max_length=300)),
                ('company_name', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
    ]
