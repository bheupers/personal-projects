from modeltranslation.translator import translator, TranslationOptions
from .models import Page, Post


class PageTranslationOptions(TranslationOptions):
    fields = ('body',) # Trailing comma is required to interpret as list

translator.register(Page, PageTranslationOptions)

class PostTranslationOptions(TranslationOptions):
    fields = ('body', 'title',) # Trailing comma is required to interpret as list

translator.register(Post, PostTranslationOptions)