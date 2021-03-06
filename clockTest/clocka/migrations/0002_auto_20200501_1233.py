# Generated by Django 3.0.5 on 2020-05-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clocka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='dakatime',
            name='uname',
        ),
        migrations.AddField(
            model_name='dakatime',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dakatime',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dakatime',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
