from django.contrib import admin
from models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
    fieldsets = [
        ('base', {'fields': ['id', 'btitle']}),
        ('super', {'fields': ['bpub_date']})
    ]


# Register your models here.

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
