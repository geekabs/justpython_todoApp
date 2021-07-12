'''
DB機能
'''
from django.db import models


class Todo(models.Model):
    
    title = models.CharField('タイトル',max_length=50)
    body = models.TextField('内容', max_length=200)
    created = models.DateTimeField('作成日時',auto_now=True)
    updated = models.DateTimeField('更新日時',auto_now=True)
    
    def __str__(self):
        return self.title