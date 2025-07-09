from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'subtitle')
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'content', 'image')
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Service, ServiceAdmin)
