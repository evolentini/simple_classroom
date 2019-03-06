# -*- coding: utf-8 -*-
from django.contrib import admin
from simple_classroom.apps.bibliography.models import Book, GroupCategory


@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subject', 'editorial', 'order')
    list_filter = ('subject', )

