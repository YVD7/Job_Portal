from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import JobListingForm, ApplicationForm
from .models import JobListing, Application



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def post_job(request):
    if request.method == "POST":
        form = JobListingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect("job_list")
    else:
        form = JobListingForm()
    return render(request, 'jobs/post_job.html', {'form': form})


def job_list(request):
    jobs = JobListingForm.objects.all()

    # Apply filter
    location_filter = request.GET.get('location')
    if location_filter:
        jobs = jobs.filter(location_icontains=location_filter)

    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    if request.method == "POST":
        application = Application(job=job, seeker=request.user)
        application.save()
        return redirect('job_list')
    return render(request, 'jobs/apply_for_jobs.html', {'job': job})