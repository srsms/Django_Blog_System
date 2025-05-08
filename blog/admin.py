from django.contrib import admin
from .models import Post, Tag
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'display_tags', 'image_preview')
    list_filter = ('author', 'date_posted', 'tags')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    
    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)