from django.db import models


class STORE(models.Model):
    Store_Number = models.CharField(max_length=50, primary_key=True)
    Phone_Number = models.CharField(max_length=10)
    Street_Address = models.CharField(max_length=200)
    Has_Restaurant = models.BooleanField(default=False)
    Has_Snack_Bar = models.BooleanField(default=False)
    Time_Limit = models.ForeignKey('CHILDCARE', on_delete= models.RESTRICT, db_column = 'Time_Limit')
    State_Location = models.ForeignKey('CITY',
                                       on_delete= models.RESTRICT,
                                       db_column = 'State_Location',
                                       related_name="fk_STORE_StateLocation_CITY_StateLocation")
    City_Name = models.ForeignKey('CITY',
                                  on_delete= models.RESTRICT,
                                  db_column='City_Name',
                                  related_name="fk_STORE_CityName_CITY_CityName")

    class Meta:
        db_table = 'store'


class CHILDCARE(models.Model):
    Time_Limit = models.IntegerField()

    class Meta:
        db_table = 'childcare'


class CITY(models.Model):
    State_Location = models.CharField(max_length=50)
    City_Name = models.CharField(max_length=50)
    Population = models.IntegerField()

    class Meta:
        db_table = 'city'


class PRODUCT(models.Model):
    PID = models.CharField(max_length=50)
    Product_Name = models.CharField(max_length=50)
    Retail_Price = models.FloatField()

    class Meta:
        db_table = 'product'


class SELL(models.Model):
    Store_Number = models.ForeignKey(STORE, on_delete= models.CASCADE, db_column='Store_Number')
    PID = models.ForeignKey(PRODUCT, on_delete= models.CASCADE, db_column='PID')

    class Meta:
        db_table = 'sell'


class DAY(models.Model):
    Date = models.DateField(primary_key= True)

    class Meta:
        db_table = 'day'


class SALE(models.Model):
    Date = models.ForeignKey(DAY, on_delete= models.CASCADE, db_column='Date')
    Store_Number = models.ForeignKey(STORE, on_delete=models.CASCADE, db_column='Store_Number')
    PID = models.ForeignKey(PRODUCT, on_delete=models.CASCADE, db_column='PID')
    Total_Amount = models.FloatField()

    class Meta:
        db_table = 'sale'


class CATEGORY(models.Model):
    Category_Name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'


class ASSIGNED(models.Model):
    PID = models.ForeignKey(PRODUCT, on_delete=models.CASCADE, db_column='PID')
    Category_Name = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, db_column='Category_Name')

    class Meta:
        db_table = 'assigned'


class HOLIDAY(models.Model):
    Date = models.ForeignKey(DAY, on_delete= models.CASCADE, db_column='Date')
    Name = models.CharField(max_length=50, db_column='Name', primary_key=True)

    class Meta:
        db_table = 'holiday'


class DISCOUNT(models.Model):
    Date = models.ForeignKey(DAY, on_delete= models.CASCADE, db_column='Date')
    PID = models.ForeignKey(PRODUCT, on_delete=models.CASCADE, db_column='PID')
    Discount_Price = models.FloatField()

    class Meta:
        db_table = 'discount'


class ADVERTISIN_GCAMPAIGN(models.Model):
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'advertising_campaign'


class HOLD(models.Model):
    Date = models.ForeignKey(DAY, on_delete= models.CASCADE, db_column='Date')
    Description = models.ForeignKey(ADVERTISIN_GCAMPAIGN, on_delete=models.CASCADE, db_column='Description')

    class Meta:
        db_table = 'hold'

