from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_img',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_at']
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content= models.CharField(max_length=200)


    def __str__(self):
        return self.content

    
    

   
