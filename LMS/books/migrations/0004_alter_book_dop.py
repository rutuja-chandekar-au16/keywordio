# Generated by Django 4.0.5 on 2022-06-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_dop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='DOP',
            field=models.DateField(),
        ),
    ]