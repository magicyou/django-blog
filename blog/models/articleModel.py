from django.db import models

# 文章表
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default='没有名字')
    cateId = models.PositiveIntegerField(default=1)
    content = models.TextField(null=True,default='暂无内容')
    create_time = models.DateTimeField(null=True)
    create_user = models.CharField(max_length=32,default='没有名字')

    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.title