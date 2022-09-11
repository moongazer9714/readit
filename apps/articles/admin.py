from django.contrib import admin

# Register your models here.


from .models import Category, Tag, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category',)
    date_hierarchy = 'created_at'


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
