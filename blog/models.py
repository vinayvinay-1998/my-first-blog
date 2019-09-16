from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author         = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete =models.CASCADE)
    title          = models.CharField(max_length=120)
    text           = models .TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=False,null=True)
    

    def Publish(self):
        self.published_date =timezone.now
        self.save()
    def _str_(self):
        return self.title
