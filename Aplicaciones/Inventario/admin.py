from django.contrib import admin
from .models import Teclado,Raton,Monitor,Computador,Post
# Register your models here.
admin.site.register(Raton)
admin.site.register(Teclado)
admin.site.register(Monitor)
admin.site.register(Computador)
admin.site.register(Post)
