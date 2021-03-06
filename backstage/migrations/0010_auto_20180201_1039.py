# Generated by Django 2.0 on 2018-02-01 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0009_auto_20180126_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_to', to='backstage.Comment'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'IN DRAFTS'), (2, 'PUBLISHED'), (0, 'DELETED')], default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='belonged_pub_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, related_name='comments', related_query_name='comments', to='backstage.PublishedArticle', to_field='pub_id'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='backstage.Comment'),
        ),
    ]
