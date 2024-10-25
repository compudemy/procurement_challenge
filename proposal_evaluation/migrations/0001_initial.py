# Generated by Django 5.1.2 on 2024-10-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='proposals/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('evaluated', models.BooleanField(default=False)),
            ],
        ),
    ]
