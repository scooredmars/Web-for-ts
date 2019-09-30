from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Author"),
        on_delete=models.CASCADE
    )

    title = models.CharField(verbose_name=_("Title"), max_length=200)
    text = models.TextField(verbose_name=_("Text"))

    created_date = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )
    published_date = models.DateTimeField(
        verbose_name=_("Published on"),
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
