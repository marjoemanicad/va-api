# Generated by Django 3.2.5 on 2022-10-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_userlogs_earned_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
