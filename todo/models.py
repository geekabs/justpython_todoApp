'''
DB機能
'''
from django.db import models
from django.utils import timezone
import uuid


class Todo(models.Model):
    
    title = models.CharField('タイトル',max_length=50)
    body = models.TextField('内容', max_length=200)
    created = models.DateTimeField('作成日時',auto_now=True)
    updated = models.DateTimeField('更新日時',auto_now=True)
    
    def __str__(self):
        return self.title


# # 投稿記事テーブル
# class Article(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     date = models.DateField(verbose_name='日付', default=timezone.now)
#     title = models.CharField(verbose_name='タイトル', max_length=40)
#     text = models.CharField(verbose_name='本文', max_length=200)
#     created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
#     updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)