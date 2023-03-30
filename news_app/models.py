from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    about = models.TextField()
    twitter = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class News(models.Model):
    headline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    created = models.CharField(max_length=100)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Podcast(models.Model):
    headline = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    created = models.CharField(max_length=100)

    def __str__(self):
        return self.headline
        
    class Meta:
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'

