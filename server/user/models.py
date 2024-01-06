from django.db import models


class User(models.Model):
    user = models.IntegerField(unique=True)
    group = models.TextField()
    nickname = models.TextField(null=True)
    name = models.TextField(null=True)
    sno = models.TextField(null=True)
    tel = models.TextField(null=True)
    email = models.TextField(null=True)
    gender = models.TextField(null=True)
    qq = models.TextField(null=True)
    website = models.TextField(null=True)
    school = models.TextField(null=True)
    grade = models.TextField(null=True)
    major = models.TextField(null=True)
    campus = models.TextField(null=True)
    aff = models.TextField(null=True)
    token = models.TextField()
    suspicious = models.BooleanField(default=False)
    suspicious_reason = models.TextField(null=True)
    suspicious_ddl = models.DateTimeField(null=True)

    class Meta:
        default_permissions = ()
        permissions = [
            ('full', '管理个人信息'),
            ('view', '查看个人信息'),
            ('view_ljyz', '查看连江一中个人信息'),
        ]


class UserLog(models.Model):
    context_user = models.IntegerField(null=True)
    context_time = models.DateTimeField()
    context_elevated = models.BooleanField()
    user = models.IntegerField()
    group = models.TextField()
    nickname = models.TextField(null=True)
    name = models.TextField(null=True)
    sno = models.TextField(null=True)
    tel = models.TextField(null=True)
    email = models.TextField(null=True)
    gender = models.TextField(null=True)
    qq = models.TextField(null=True)
    website = models.TextField(null=True)
    school = models.TextField(null=True)
    grade = models.TextField(null=True)
    major = models.TextField(null=True)
    campus = models.TextField(null=True)
    aff = models.TextField(null=True)
    token = models.TextField()
    suspicious = models.BooleanField(default=False)
    suspicious_reason = models.TextField(null=True)
    suspicious_ddl = models.DateTimeField(null=True)

    class Meta:
        default_permissions = ()
