from django.db import models
from django.utils import timezone
POST_TYPE =(
    ('Draft','Draft'),
    ('Published','Published'),
)

class Post(models.Model):
    title = models.TextField(max_length=50, unique=True)
    content = models.CharField(max_length=2000, null=True)
    email = models.EmailField(default='')
    phone = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    type = models.CharField(choices=POST_TYPE, default='Draft',max_length=20)
    image=models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title

