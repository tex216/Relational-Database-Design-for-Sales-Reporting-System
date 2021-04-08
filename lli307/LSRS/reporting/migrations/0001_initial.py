# Generated by Django 3.1.7 on 2021-03-30 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADVERTISIN_GCAMPAIGN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'advertising_campaign',
            },
        ),
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CHILDCARE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time_Limit', models.IntegerField()),
            ],
            options={
                'db_table': 'childcare',
            },
        ),
        migrations.CreateModel(
            name='CITY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_Location', models.CharField(max_length=50)),
                ('City_Name', models.CharField(max_length=50)),
                ('Population', models.IntegerField()),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='DAY',
            fields=[
                ('Date', models.DateField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'day',
            },
        ),
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.CharField(max_length=50)),
                ('Product_Name', models.CharField(max_length=50)),
                ('Retail_Price', models.FloatField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='STORE',
            fields=[
                ('Store_Number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('Street_Address', models.CharField(max_length=200)),
                ('Has_Restaurant', models.BooleanField(default=False)),
                ('Has_Snack_Bar', models.BooleanField(default=False)),
                ('City_Name', models.ForeignKey(db_column='City_Name', on_delete=django.db.models.deletion.RESTRICT, related_name='fk_STORE_CityName_CITY_CityName', to='reporting.city')),
                ('State_Location', models.ForeignKey(db_column='State_Location', on_delete=django.db.models.deletion.RESTRICT, related_name='fk_STORE_StateLocation_CITY_StateLocation', to='reporting.city')),
                ('Time_Limit', models.ForeignKey(db_column='Time_Limit', on_delete=django.db.models.deletion.RESTRICT, to='reporting.childcare')),
            ],
            options={
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='SELL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.ForeignKey(db_column='PID', on_delete=django.db.models.deletion.CASCADE, to='reporting.product')),
                ('Store_Number', models.ForeignKey(db_column='Store_Number', on_delete=django.db.models.deletion.CASCADE, to='reporting.store')),
            ],
            options={
                'db_table': 'sell',
            },
        ),
        migrations.CreateModel(
            name='SALE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Amount', models.FloatField()),
                ('Date', models.ForeignKey(db_column='Date', on_delete=django.db.models.deletion.CASCADE, to='reporting.day')),
                ('PID', models.ForeignKey(db_column='PID', on_delete=django.db.models.deletion.CASCADE, to='reporting.product')),
                ('Store_Number', models.ForeignKey(db_column='Store_Number', on_delete=django.db.models.deletion.CASCADE, to='reporting.store')),
            ],
            options={
                'db_table': 'sale',
            },
        ),
        migrations.CreateModel(
            name='HOLIDAY',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(db_column='Name', max_length=50)),
                ('Date', models.ForeignKey(db_column='Date', on_delete=django.db.models.deletion.CASCADE, to='reporting.day')),
            ],
            options={
                'db_table': 'holiday',
            },
        ),
        migrations.CreateModel(
            name='HOLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.ForeignKey(db_column='Date', on_delete=django.db.models.deletion.CASCADE, to='reporting.day')),
                ('Description', models.ForeignKey(db_column='Description', on_delete=django.db.models.deletion.CASCADE, to='reporting.advertisin_gcampaign')),
            ],
            options={
                'db_table': 'hold',
            },
        ),
        migrations.CreateModel(
            name='DISCOUNT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discount_Price', models.FloatField()),
                ('Date', models.ForeignKey(db_column='Date', on_delete=django.db.models.deletion.CASCADE, to='reporting.day')),
                ('PID', models.ForeignKey(db_column='PID', on_delete=django.db.models.deletion.CASCADE, to='reporting.product')),
            ],
            options={
                'db_table': 'discount',
            },
        ),
        migrations.CreateModel(
            name='ASSIGNED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.ForeignKey(db_column='Category_Name', on_delete=django.db.models.deletion.CASCADE, to='reporting.category')),
                ('PID', models.ForeignKey(db_column='PID', on_delete=django.db.models.deletion.CASCADE, to='reporting.product')),
            ],
            options={
                'db_table': 'assigned',
            },
        ),
    ]