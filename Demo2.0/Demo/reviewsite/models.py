from django.db import models


# Create your models here.

class Sex(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class Position(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class UserType(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class RegionType(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class UsersInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)
    introduction = models.TextField()
    company = models.CharField(max_length=20)#单位
    position = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    region = models.CharField(max_length=20)
    research = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)


class PaperInfo(models.Model):
    title = models.CharField(max_length=40)
    authorID = models.ForeignKey(UsersInfo, on_delete=models.DO_NOTHING)
    #author = models.CharField(max_length=40)
    authorname_1 = models.CharField(max_length=20, null=False)#非空，其他全空
    authorname_2 = models.CharField(max_length=20, null=True)
    authorname_3 = models.CharField(max_length=20, null=True)
    authorname_4 = models.CharField(max_length=20, null=True)
    authorname_5 = models.CharField(max_length=20, null=True)
    abstract = models.TextField()
    research = models.CharField(max_length=100)#
    paperfile = models.FileField(upload_to='paper')#上传paper 让审稿人下载
    state = models.CharField(max_length=20, default="未分配")#审核状态，审稿人（手动切换h5，下拉栏，默认审稿中，接受，拒绝），（主编通过，退回）

    def __str__(self):
        return str(self.pk)


class ExpertReview(models.Model):
    paperID = models.CharField(max_length=20)
    expertID = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    opinion = models.TextField()


class EditorReview(models.Model):
    paperID = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    opinion = models.TextField()

class Allocate(models.Model):
    PaperID = models.CharField(max_length=20)
    ExpertID_1 = models.CharField(max_length=20)
    ExpertID_2 = models.CharField(max_length=20)
    ExpertID_3 = models.CharField(max_length=20)