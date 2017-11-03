from __future__ import unicode_literals

from django.db import models


class Post(models.Model):

    """Model definition for Post."""
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:

        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        """Unicode representation of Post."""
        return self.title
