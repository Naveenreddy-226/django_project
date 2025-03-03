# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# # Create your models here.
# class Post(models.Model):
#     title=models.CharField(max_length=100)
#     content=models.TextField()
#     date_posted=models.DateTimeField(default=timezone.now)
#     author=models.ForeignKey(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    


from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


