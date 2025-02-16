from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    # 作者，关联到Django的用户模型
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    # 标题，最大长度为200字符
    title = models.CharField(max_length=200)

    # 文章内容，使用TextField来存储长文本
    text = models.TextField()

    # 创建日期，默认值为当前时间
    created_date = models.DateTimeField(default=timezone.now)

    # 发布日期，可以为空
    published_date = models.DateTimeField(blank=True, null=True)

    # 文章摘要，可以为空
    excerpt = models.TextField(blank=True, null=True)

    # 文章状态
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def publish(self):
        # 将发布日期设置为当前时间，并保存模型
        self.published_date = timezone.now()
        self.status = 'published'
        self.save()

    def __str__(self):
        # 返回文章标题作为字符串表示
        return self.title

    # 返回文章是否已发布
    def is_published(self):
        return self.status == 'published' and self.published_date is not None

    # 自定义管理器
    @classmethod
    def published(cls):
        return cls.objects.filter(status='published', published_date__isnull=False)

    class Meta:
        # 按创建日期排序
        ordering = ['-created_date']
        # 指定模型的verbose_name
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'