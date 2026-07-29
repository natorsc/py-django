from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "complete", "created_at", "updated_at")
    list_filter = ("complete", "created_at")
    search_fields = ("title",)
    list_editable = ("complete",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
