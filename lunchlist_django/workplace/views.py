from django.shortcuts import render
from workplace.models import WorkPlace
# Create your views here.
def index(request):

    work_list = WorkPlace.objects.all()
    work_dict = {'work_name':work_list}


    return render(request,'workplace/index.html',work_dict)