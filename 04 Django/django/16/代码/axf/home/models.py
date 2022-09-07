# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AxfCart(models.Model):
    c_goods_num = models.IntegerField()
    c_is_select = models.IntegerField()
    c_goods = models.ForeignKey('AxfGoods', models.DO_NOTHING, blank=True, null=True)
    c_user = models.ForeignKey('AxfUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axf_cart'


class AxfFoodtype(models.Model):
    typeid = models.IntegerField()
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=255)
    typesort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_foodtype'


class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=255)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=255)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=64)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=128)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_goods'


class AxfMainshow(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=64)
    img1 = models.CharField(max_length=255)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=255)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=255)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'axf_mainshow'


class AxfMustbuy(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_mustbuy'


class AxfNav(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_nav'


class AxfOrder(models.Model):
    o_price = models.FloatField()
    o_time = models.DateTimeField()
    o_status = models.IntegerField()
    o_user = models.ForeignKey('AxfUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axf_order'


class AxfOrdergoods(models.Model):
    o_goods_num = models.IntegerField()
    o_goods = models.ForeignKey(AxfGoods, models.DO_NOTHING, blank=True, null=True)
    o_order = models.ForeignKey(AxfOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axf_ordergoods'


class AxfShop(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_shop'


class AxfUser(models.Model):
    u_username = models.CharField(unique=True, max_length=32)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(unique=True, max_length=64)
    is_active = models.IntegerField(default=1)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_user'


class AxfWheel(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axf_wheel'


