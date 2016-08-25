# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.TextField(default='')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='lists.List'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
