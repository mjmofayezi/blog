from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    article = models.FileField(blank=True, upload_to='files/articles/')
    image = models.ImageField(upload_to='files/images/')
    link = models.CharField(max_length=200)
    date = models.DateField()
    auther = ""
    time_to_read = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("article_detail", args=[str(self.id)])
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    # def get_absolute_url(self):
    #      return reverse("article_detail", kwargs={"slug": self.slug})
    def get_absolute_url(self):
         return reverse("post_detail", args=[str(self.slug)])     


@receiver(pre_save, sender=Post)
def pre_save_article_receiver(sender,instance,*args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug
    