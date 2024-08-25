from django.contrib import admin
from .models import Project
# Register your models here.
admin.site.register(Project) #este comando es para decirle a django que atravs de su administrador me administre los projectos
