from django.db import models

# 分类表
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='没有名字')
    userId = models.PositiveIntegerField(null=False)
    create_time = models.DateTimeField(null=True)
    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.name