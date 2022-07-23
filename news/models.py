from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    text = models.TextField()
    main_image = models.ImageField(upload_to='news_img/')
    date = models.CharField(max_length=40, default='05/07/2022')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'id.{}: {}'.format(self.id, self.title)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-id']


class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='news_img/')

    def __str__(self):
        return 'image id:{}, for news{}'.format(self.id, self.news)
