from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
