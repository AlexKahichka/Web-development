from django.contrib import admin
# Register your models here.
from django.contrib import admin
from my_app.models.task import Task, SubTask, Category

admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Category)