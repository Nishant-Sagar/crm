# Generated by Django 3.1.1 on 2020-09-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200915_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
