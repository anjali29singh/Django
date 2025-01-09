from django.db import models
# blog data model 

class User(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField()


class Blog(models.Model):

    #Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True)
    body = models.TextField()

    
    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk}

