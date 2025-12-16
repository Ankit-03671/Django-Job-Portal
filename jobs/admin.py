from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'salary', 'posted_by', 'created_at']
    list_filter = ['created_at', 'location', 'company_name']
    search_fields = ['title', 'company_name', 'description']
    readonly_fields = ['created_at']
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_module_permission(self, request):
        return request.user.is_superuser
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new job
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'applied_at']
    list_filter = ['applied_at', 'job__company_name']
    search_fields = ['applicant__username', 'job__title']
    readonly_fields = ['applied_at']