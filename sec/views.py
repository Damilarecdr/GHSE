from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide, Update, Whyu, Teacher, School_Info, Welcome




#def about(request):
 #   return render(request, 'about.html')  # New view function for the "About" page

def home(request):
    slides = Slide.objects.filter(is_active=True) 
    update =  Update.objects.first()
    whyu = Whyu.objects.all()
    teacher = Teacher.objects.all()
    school_Info = School_Info.objects.first() 
    welcome = Welcome.objects.first() 
    
    context = {
        'slides': slides,
        'update': update,
        'whyu' : whyu,
        'teacher' : teacher,
        'school_info' : school_Info,
        'welcome' : welcome,
        

    }

    return render(request, 'home.html', context)
