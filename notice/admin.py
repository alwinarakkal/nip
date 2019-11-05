from django.contrib import admin
from .models import Post,Comment
# Register your models here.







class PostAdmin(admin.ModelAdmin):
  list_display = [
      'aut',
      'created_on',
  ]



class CommentAdmin(admin.ModelAdmin):
  list_display = [
      'author',
      'post',
      'created_on',
     
  ]
search_fields = ['author']


admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)