from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserScheduleForm
from django.http.response import HttpResponseRedirect
from .models import User, UserSchedule

# Create your views here.
def index(request):
    return HttpResponse("ajklsdfhaoghis,lamgho;aerighslkdfh")
def activityschedule(request):
    #return HttpResponse("show the table here")
    if request.method == 'POST':
        form = UserScheduleForm(request.POST)
        #use the user id after integrating this to the main project; for now hardcode
        user = User.objects.get(id=request.POST.get('user'))
        userschedule, created = UserSchedule.objects.get_or_create(user=user, week=request.POST.get('week'))
        userschedule.sleeping = request.POST.get('sleeping')
        userschedule.rumination = request.POST.get('rumination')
        userschedule.mastery = request.POST.get('mastery')
        userschedule.pleasure = request.POST.get('pleasure')
        userschedule.distractionAndAvoidance = request.POST.get('distractionAndAvoidance')
        userschedule.miscellaneous = request.POST.get('miscellaneous')
        userschedule.save()
        message = 'form submitted'
        return render(request, 'behavioralactivation/activityschedule.html', {'message': message})
        """
        if not userschedule.exists():
            #userschedulenew = UserSchedule.objects.filter(user=user).get_or_create(week=request.POST.get('week'))
            userschedulenew = UserSchedule.objects.create(week = request.POST.get('week'), user=user)
            userschedulenew = UserSchedule(sleeping=request.POST.get('sleeping'), rumination=request.POST.get('rumination'))
            userschedulenew.save()
        else:
            userschedule = UserSchedule.objects.get(week=request.POST.get('week'), user=user)
            userschedule.sleeping = request.POST.get('sleeping')
            userschedule.rumination = request.POST.get('rumination')
            userschedule.mastery = request.POST.get('mastery')
            userschedule.pleasure = request.POST.get('pleasure')
            userschedule.distractionAndAvoidance = request.POST.get('distractionAndAvoidance')
            userschedule.miscellaneous = request.POST.get('miscellaneous')
            userschedule.week = request.POST.get('week')
            userschedule.save()
        #if form.is_valid():
            return HttpResponse(request.POST.get('rumination'))
        """ 
    else:
        form = UserScheduleForm()
       
    return render(request, 'behavioralactivation/activityschedule.html', {'form':form})
    
