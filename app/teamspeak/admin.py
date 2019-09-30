from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "text",
                    "created_date", "published_date"]
    list_display_links = ["published_date"]
    list_editable = ["title"]
    list_filter = ["created_date", "published_date"]

    search_fields = ["title", "text"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
