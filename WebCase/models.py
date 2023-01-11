from django.db import models


class CaseUser(models.Model):
    """用户表"""
    username = models.CharField(verbose_name="用户名称", max_length=64)
    password = models.CharField(verbose_name="用户密码", max_length=64)

    def __str__(self):
        return self.username


class CaseModel(models.Model):
    """所属模块库"""
    modelName = models.CharField(verbose_name="模块名称", max_length=64)
    modelDate = models.DateField(verbose_name="模块创建时间")

    def __str__(self):
        return self.modelName


class Case(models.Model):
    """用例库"""
    caseName = models.CharField(verbose_name="用例标题", max_length=64)
    caseModel = models.ForeignKey(verbose_name="所属模块", to='CaseModel', to_field="id", on_delete=models.CASCADE)
    caseCreator = models.ForeignKey(verbose_name="创建人", to='CaseUser', to_field="id", on_delete=models.CASCADE)
    caseExecutor = models.ForeignKey(CaseUser, related_name='person_user', on_delete=models.CASCADE)
    caseDate = models.DateField(verbose_name="用例创建时间")
    case_choices = (
        (1, '已执行'),
        (2, '未执行')
    )
    caseChoices = models.SmallIntegerField(verbose_name="用例执行状态", choices=case_choices, default=2)
