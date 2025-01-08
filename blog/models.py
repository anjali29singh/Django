from django.db import models
# blog data model 

class Blog(models.Model):

    #Fields
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    
    class Meta:
        ordering=['-created_at']

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk}