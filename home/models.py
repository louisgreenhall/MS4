from django.db import models

class Request(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    status = models.CharField(max_length=50)
    draw_type = models.CharField(max_length=255, default='')
    colour = models.CharField(max_length=255, default='')
    backing = models.CharField(max_length=255, default='')
    files = models.CharField(max_length=255, default='')
    def get_absolute_url(self):
        return '/requests/' + str(self.id)
    def save(self, *args, **kwargs):
        # If I need to do anything before it saves
        super(Request, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title
