from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model  # from user.models import UserProfile
from goods.models import Goods

User = get_user_model()


# Create your models here.

class ShoppingCart(models.Model):
    '''購物車'''
    user = models.ForeignKey(User, verbose_name='用戶', null=True, on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, verbose_name='商品', null=True, on_delete=models.SET_NULL)
    goods_num = models.IntegerField(default=0, verbose_name='商品數量')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '購物車'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s(%d)'.format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    '''訂單信息'''
    ORDER_STATUS = (
        ('success', '成功'),
        ('cancel', '取消'),
        ('paying', '待支付'),
    )
    user = models.ForeignKey(User, verbose_name='用戶', null=True, on_delete=models.SET_NULL)
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='訂單號')
    trade_no = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name='交易號')
    pay_status = models.CharField(max_length=100, choices=ORDER_STATUS, verbose_name='訂單狀態')
    pay_script = models.CharField(max_length=50, verbose_name='訂單留言')
    order_mount = models.FloatField(default=0.0, verbose_name='訂單金額')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付時間')

    # 用戶基本信息
    address = models.CharField(max_length=100, default='', verbose_name='收貨地址')
    signer_name = models.CharField(max_length=20, default='', verbose_name='收件人')
    signer_mobile = models.CharField(max_length=10, verbose_name='聯絡電話')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    '''訂單商品詳情'''
    order = models.ForeignKey(OrderInfo, verbose_name='訂單信息', null=True, on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, verbose_name='商品', null=True, on_delete=models.SET_NULL)
    goods_num = models.IntegerField(default=0, verbose_name='商品數量')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '訂單商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
