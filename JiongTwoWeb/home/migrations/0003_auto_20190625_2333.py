# Generated by Django 2.2.2 on 2019-06-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190625_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='jtuserprofile',
            name='birthday',
            field=models.DateTimeField(auto_now=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='jtuserprofile',
            name='sex',
            field=models.CharField(choices=[('0', '保密'), ('1', '男'), ('2', '女')], default=0, max_length=5, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='jtuserprofile',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', max_length=255, upload_to='avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]
