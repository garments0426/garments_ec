"""
加載 category_data 文件
"""


import sys
import os

# 先配置路徑
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

import django

django.setup()  # 外部腳本調用django環境

# ======================================
from goods.models import GoodsCategory

from db_tools.data.category_data import row_data

for lev1 in row_data.values():
    for lev2 in lev1:
        lev2_instance = GoodsCategory()
        lev2_instance.code = lev2['code']
        lev2_instance.name = lev2['name']
        lev2_instance.category_type = 1
        lev2_instance.save()

print('Category data imported successfully')
