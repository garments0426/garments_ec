from django.db import models
from DjangoUeditor.models import UEditorField
from datetime import datetime


# Create your models here.

class GoodsCategory(models.Model):
    '''商品分類'''
    CATEGORY_TYPE = (
        (1, '一級類目 '),
        (2, '二級類目 '),
        (3, '三級類目 '),
    )
    name = models.CharField(max_length=30, default='', verbose_name='類別名', help_text='類別名')
    code = models.CharField(max_length=30, default='', verbose_name='類別code', help_text='類別code')
    desc = models.TextField(default='', verbose_name='類別描述', help_text='類別描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='類目級別', help_text='類目級別')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父類別', related_name='sub_cat',
                                        on_delete=models.SET_NULL)
    is_tab = models.BooleanField(default=False, verbose_name='是否導航', help_text='是否導航')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '商品類別'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodCategoryBrand(models.Model):
    '''品牌名'''
    name = models.CharField(max_length=50, default='', verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(max_length=300, default='', verbose_name='品牌描述', help_text='品牌描述')
    image = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='使否刪除')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''商品'''
    category = models.ForeignKey(GoodsCategory, verbose_name='商品類目', null=True, on_delete=models.SET_NULL)
    #goods_size = models.TextField(max_length=5, verbose_name='尺寸')
    goods_sh = models.CharField(max_length=50, default='', verbose_name='商品唯一編號')
    name = models.CharField(max_length=300, verbose_name='商品名')
    click_num = models.IntegerField(default=0, verbose_name='點擊量')
    sold_num = models.IntegerField(default=0, verbose_name='銷售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏量')
    goods_num = models.IntegerField(default=0, verbose_name='庫存量')
    shop_price = models.FloatField(default=0, verbose_name='本店價格')
    goods_brief = models.TextField(max_length=500, verbose_name='商品簡介')
    goods_desc = UEditorField(verbose_name=u'內容', imagePath='goods/images/', width=1000, height=300,
                              filePath='goods/files/', default='')
    ship_free = models.BooleanField(default=True, verbose_name='是否承擔運費')
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面圖')
    is_new = models.BooleanField(default=False, verbose_name='是否新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否熱銷')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class GoodsImage(models.Model):
    '''商品輪播圖'''
    goods = models.ForeignKey(Goods, verbose_name='', related_name='商品', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='圖片')
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name='圖片連接')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '商品輪播圖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    '''輪播商品'''
    goods = models.ForeignKey(Goods, verbose_name='商品', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='banner', verbose_name='輪播圖片')
    index = models.IntegerField(default=0, verbose_name='輪播順序')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加時間')
    is_delete = models.BooleanField(default=False, verbose_name='是否刪除')

    class Meta:
        verbose_name = '輪播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
