from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    #最新文章
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    # 归档
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 分类
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
 
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 获取标签
   return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)