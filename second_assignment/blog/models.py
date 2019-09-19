from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)            #title의 속성은 최대 200자의 문자열 (짧은 문장)
    pub_data = models.DateTimeField('data published')   #날짜와, 시간속성
    body = models.TextField()                           #body는 긴 문자열

    def __str__(self):
        return self.title