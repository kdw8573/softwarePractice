from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    sinceWhen = models.DateTimeField()
    tilWhen = models.DateTimeField()
    user =  models.ForeignKey('auth.User', related_name='meetings',on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ['id','created','sinceWhen','tilWhen','user']

    def save(self, *args, **kwargs):
        super(Meeting, self).save(*args, **kwargs)
