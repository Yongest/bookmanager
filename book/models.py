from django.db import models

# Create your models here.
"""
1.定义模型类
2.模型迁移
    2.1生成迁移文件（不会在数据库中生成表）
    python manage.py makemigrations
    如果未注册app，那么 会显示 No changes detected
    2.2 再迁移（在数据库中生成表）
    python manage.py migrate
3.数据库操作
 ORM对应关系
 表---类
 字段-----属性
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

        
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)