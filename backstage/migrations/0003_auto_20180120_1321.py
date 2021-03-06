# Generated by Django 2.0 on 2018-01-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0002_auto_20180120_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.SmallIntegerField(choices=[(2, 'PUBLISHED'), (0, 'DELETED'), (1, 'IN DRAFTS')], default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('reprint', '转载'), ('original', '原创'), ('translation', '翻译')], default='original', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_time',
            field=models.DateField(auto_now=True),
        ),
    ]
