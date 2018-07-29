from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    anthor = models.ForeignKey(User, on_delete=models.CASCADE)

    #阅读量
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *arg, **kwargs): #复写Post类的save
        if not self.excerpt:
            md = markdown.Markdown(extensions=['markdown.extensions.extra',
                'markdown.extensions.codehilite',])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*arg, **kwargs) #调用父类的save()
        