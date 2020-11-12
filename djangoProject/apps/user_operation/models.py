from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods

# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    '''用戶收藏'''
    user = models.ForeignKey(User, verbose_name='用戶', null=True, on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, verbose_name='商品', null=True, on_delete=models.SET_NULL)

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '用戶收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    '''用戶留言'''
    MESSAGE_CHOICES = (
        (1, '留言'),
        (2, '詢問'),
        (3, '售後'),
        (4, '求購'),
    )
    user = models.ForeignKey(User, verbose_name='用戶', null=True, on_delete=models.SET_NULL)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name='留言類型',
                                       help_text='留言類型: 1(留言),2(詢問),3(售後),4(求購)')
    subject = models.CharField(max_length=80, default='', verbose_name='主題')
    message = models.TextField(default='', verbose_name='留言內容', help_text='留言內容')
    file = models.FileField(verbose_name='上傳的文件', help_text='上傳的文件')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '用戶留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    '''用戶收貨地址'''
    user = models.ForeignKey(User, verbose_name='用戶', null=True, on_delete=models.SET_NULL)
    district = models.CharField(max_length=50, default='', verbose_name='區域')
    address = models.CharField(max_length=100, default='', verbose_name='詳細地址')
    signer_name = models.CharField(max_length=20, default='', verbose_name='收件人')
    signer_mobile = models.CharField(max_length=10, default='', verbose_name='聯絡電話')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '收貨地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
