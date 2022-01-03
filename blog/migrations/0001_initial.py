# Generated by Django 4.0 on 2022-01-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('target_mdfile', models.CharField(max_length=255)),
                ('created_datetime', models.DateTimeField(blank=True, null=True)),
                ('updated_datetime', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'posts',
                'managed': False,
            },
        ),
    ]
