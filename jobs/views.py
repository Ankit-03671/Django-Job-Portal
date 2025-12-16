from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Q
from .models import Job, Application

def job_list(request):
    query = request.GET.get('q')
    location = request.GET.get('location')
    jobs = Job.objects.all().order_by('-created_at')
    
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query)
        )
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs})



@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        cover_letter = request.FILES.get('cover_letter')
        
        obj, created = Application.objects.get_or_create(
            job=job,
            applicant=request.user,
            defaults={'resume': resume, 'cover_letter': cover_letter}
        )
        
        if created:
            messages.success(request, 'Successfully applied for job')
        else:
            messages.info(request, 'You already applied for this job')
        return redirect('job_list')
    
    return render(request, 'jobs/apply_job.html', {'job': job})

@login_required
def seeker_dashboard(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'dashboard/seeker_dashboard.html', {'applications': applications})


