# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Mini Project 4

from django.contrib import admin
from .models import ContactMessage, Service, Project, About

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

