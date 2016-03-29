#coding:utf-8
from django.contrib import admin
from models import Author,Tag,Classification,Article

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Classification)


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
      class Media:
         js = (

         '/static/tinymce/tinymce.min.js',
         '/static/tinymce/config.js',

         )
admin.site.register(Article,ArticleAdmin)
# admin.site.register(Article)