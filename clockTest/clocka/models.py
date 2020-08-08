from django.db import models
# Create your models here.

# 一个类就对应数据库的一张表
class User(models.Model):
    # 一个属性对应一个字段
    username=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    # # 指定表的名字
    # class Mate:
    #     db_table='user'
    #     ordering=['age','name']

class DakaTime(models.Model):
    username=models.CharField(max_length=100,null=True)
    count=models.IntegerField(default=0,null=True)
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<用户名：%s,打卡时间：%s>"%(self.username,self.time)

