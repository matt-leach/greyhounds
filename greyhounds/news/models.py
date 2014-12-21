from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.title
    
    def print_tags(self):
        tags = self.tags.all()
        tags = ["<a href='%s?tags=%s'>#%s</a>" % (reverse("news:index"), tag.name, tag.name) for tag in tags]
        return " ".join(tags)