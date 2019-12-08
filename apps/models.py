from django.db import models

# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=1024, help_text="问题描述")
    answer = models.CharField(max_length=100, help_text="答案的选项")
    tips = models.CharField(max_length=1024, help_text='tips')
    pngname = models.CharField(max_length=1024, help_text='png', null=True)

    class Meta:
        db_table = "question"


class Visit(models.Model):

    ip = models.CharField(max_length=20, help_text="访问的ip地址")
    visit_time = models.DateTimeField(help_text="访问时间", auto_now_add=True)
    question = models.ForeignKey(Question, help_text="访问题目页面类型", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "visit"


class AnswerInformation(models.Model):

    question = models.ForeignKey(Question, help_text="访问题目页面类型", on_delete=models.DO_NOTHING)
    ip = models.CharField(max_length=30, help_text="访问的ip地址")
    answer = models.CharField(max_length=30, help_text="选择的答案")
    create_time = models.DateTimeField(help_text="开始时间", auto_now_add=True)
    end_time = models.DateTimeField(help_text="结束时间", null=True)

    class Meta:
        db_table = "information"
