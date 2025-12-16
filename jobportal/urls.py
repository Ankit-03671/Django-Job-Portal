"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from jobs.models import Job, Application
from django.contrib.auth.models import User
from django.db.models import Count

def home(request):
    # Get statistics for homepage
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()
    total_users = User.objects.count()
    recent_jobs = Job.objects.order_by('-created_at')[:6]
    
    # Get top companies by job count
    top_companies = Job.objects.values('company_name').annotate(
        job_count=Count('id')
    ).order_by('-job_count')[:5]
    
    context = {
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'total_users': total_users,
        'recent_jobs': recent_jobs,
        'top_companies': top_companies,
    }
    return render(request, 'home.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
