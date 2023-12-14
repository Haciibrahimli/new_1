from django.shortcuts import render
from my_app.models import *


def index_view(request):
    obj = About.objects.last() #obj.name dovre salmiriq
    experiences = Experience.objects.all()
    educations = Education.objects.all() #dovre salieiriq
    interest = Interests.objects.last()
    awards = Awards.objects.all()
    sosials = SosialMedia.objects.all() 

  
    context = {

         'obj':obj,
         'experiences':experiences,
         'educations':educations,
         'interest':interest,
         'awards':awards,
         'sosials':sosials,

    }

    return render(request,'index.html',context)

