from django.contrib import admin
from . models import Post

admin.site.site_header = 'Zago Admin Area'
admin.site.site_title = 'Welcome Here'
admin.site.index_title = 'Zago'

admin.site.register(Post)
