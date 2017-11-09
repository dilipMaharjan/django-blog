from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    """Form definition for Post."""

    class Meta:

        """Meta definition for Postform."""

        model = Post
        fields = ('title', 'content')
