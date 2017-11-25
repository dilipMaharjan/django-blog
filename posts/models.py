from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


def upload_locations(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.FileField(upload_to=upload_locations, null=True, blank=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]
