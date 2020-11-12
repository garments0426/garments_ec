from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

'''
設置用戶數據模型
'''


class UserProfile(AbstractUser):
    '''用戶個人資料'''
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male',
                              verbose_name='性別')
    mobile = models.CharField(max_length=10, verbose_name='手機')
    e_mail = models.CharField(max_length=50, null=True, blank=True, verbose_name='信箱')

    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:  # 元數據
        verbose_name = '用戶'
        verbose_name_plural = '用戶'

    def __str__(self):  # 打印姓名
        return self.name


class VerifyCode(models.Model):
    '''驗證碼'''
    code = models.CharField(max_length=10, verbose_name='驗證碼')
    mobile = models.CharField(max_length=11, verbose_name='手機號碼')
    add_time = models.DateField(default=datetime.now, verbose_name='添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:  # 元數據
        verbose_name = '短信驗證碼'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
