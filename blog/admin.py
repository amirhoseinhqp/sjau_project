from django.contrib import admin
from .models import blog , category , tag , comments
# Register your models here.
#admin.site.register(blog)
admin.site.register(category)
admin.site.register(tag)
admin.site.register(comments)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at',"author")
    list_filter = ("author" ,)
    search_fields = ("title",)
    ordering = ('title',)
    date_hierarchy = "created_at"

admin.site.register(blog,BlogAdmin)