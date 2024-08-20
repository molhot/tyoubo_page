from django.db import models

# Create your models here.

class TyouboConfig(models.Model): #No installed app with label 'tyoubo_app'.
    item_type_list = [
        ('option1', '家庭用品'),
        ('option2', '非家庭用品'),
    ]
    registed_item_name = models.CharField('item_name', max_length=50)
    item_price = models.IntegerField('item_price')
    item_type = models.CharField('item_type', max_length=20, choices=item_type_list) #選択肢にできるらしい...？
    
    def __str__(self):
        return f'登録名：{self.registed_item_name} 値段：{self.item_price}'
