from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.core.files.storage import FileSystemStorage

def loadhome(request):
    return render(request,'home.html')
# def fileAction(request):
def simple_upload(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            data=json.load(myfile)
            datacount=0
            var='ATL'
            list1=[]
            # list=[i["Airport"]['Code']+"," for i in data]
            for i in data:

                if i["Airport"]['Code']==var:
                    list1.append(i)


                aname=list1[0]["Airport"]["Name"]
                context={'cons':list1,"n":aname}

            return render(request,'view.html',context)


# Create your views here.
