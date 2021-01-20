from django.db import models
from users.models import User
from pages.models import Page

# Create your models here.

class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
              'self',
              default=None,
              blank=True,
              null=True,
              on_delete=models.CASCADE,
              verbose_name='parent',
              related_name='replys'
            )
    poster = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comment')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "[%s] %s" % (self.poster, self.content)