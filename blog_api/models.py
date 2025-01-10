from django.db import models
# blog data model 
from django.contrib.auth.models import User
class Blog(models.Model):

    #Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True)
    body = models.TextField()
    author  = models.ForeignKey(User,on_delete=models.CASCADE)


    
    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk}

