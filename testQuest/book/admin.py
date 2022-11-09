from django.contrib import admin

from book.models import Title, Volume, Chapter, Tag


class VolumeAdminInline(admin.TabularInline):
    model = Volume
    extra = 1


class ChapterAdminInline(admin.TabularInline):
    model = Chapter
    extra = 1


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'ru_name', 'eng_name', 'alt_name')
    list_display_links = ('ru_name', 'eng_name', 'alt_name')
    search_fields = ('ru_name', 'eng_name', 'alt_name')
    inlines = [VolumeAdminInline]


class VolumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'title', 'price')
    list_display_links = ('number', 'title')
    search_fields = ('name',)
    inlines = [ChapterAdminInline]
    raw_id_fields = ('title',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume', 'number', 'views_counter', 'like_counter')
    list_display_links = ('volume', 'number')
    search_fields = ('number',)
    raw_id_fields = ('volume',)
    readonly_fields = ('like_counter', 'views_counter',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Title, TitleAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Tag, TagAdmin)