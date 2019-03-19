# Generated by Django 2.1 on 2019-03-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_credit_total_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remaining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_amt_total', models.IntegerField(default=0)),
                ('paid_amt_total', models.IntegerField(default=0)),
                ('userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserData')),
            ],
        ),
        migrations.RenameField(
            model_name='credit',
            old_name='remaining',
            new_name='remaining_current',
        ),
    ]
