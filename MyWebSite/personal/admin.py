from django.contrib import admin
from .models import Post, Media, Page
from modeltranslation.admin import TranslationAdmin

class PostAdmin(TranslationAdmin):
    pass

admin.site.register(Post, PostAdmin)

class PageAdmin(TranslationAdmin):
    pass

admin.site.register(Page, PageAdmin)

admin.site.register(Media)