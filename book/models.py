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
 null 是否为空
 unique 唯一
 default 设置默认值
 verbose_name admin后台显示
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True,verbose_name='名字')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=0)
    
    
    class Meta:
        # 改表名
        db_table ='bookinfo'
        verbose_name = '后台管理'

    def __str__(self):
        return self.name


        
class PeopleInfo(models.Model):
    GENDER_CHOICE=(
        (0,'male'),
        (1,'female'),
    )
    name=models.CharField(max_length=20,verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=0,verbose_name='性别')
    description = models.CharField(max_length=200,null=True,verbose_name='描述')
    # 外键,级联操作CASCADE
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书名')
    is_delete = models.BooleanField(verbose_name='删除',default=0)