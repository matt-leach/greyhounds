from django.db import models




class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return self.title