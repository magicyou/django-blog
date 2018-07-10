from django.db import models

# user用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255,null=False)
    name = models.CharField(max_length=255,null=False)
    password = models.CharField(max_length=255,null=False)
    email = models.TextField(null=True)
    address = models.DateTimeField(null=True)
    phone = models.CharField(max_length=15,null=True)

    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.nickname