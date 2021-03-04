from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register(blog)
admin.site.register(about)
admin.site.register(portfilio)