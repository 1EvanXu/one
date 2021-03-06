# Generated by Django 2.0 on 2018-03-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0020_auto_20180216_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'DELETED'), (2, 'PUBLISHED'), (1, 'IN DRAFTS')], default=1),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('original', '原创'), ('reprint', '转载'), ('translation', '翻译')], default='original', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='child_comment', to='backstage.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reply_to', to='backstage.Comment'),
        ),
    ]
