from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homePage(request):
    result = 0
    data = {}
    try:
        # num1 = int(request.GET.get('num1'))
        num1 = int(request.POST.get('num1'))
        # num2 = int(request.GET.get('num2'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
        # print (result)
        data = {
            'info': 'This data is comming dynamically.',
            'studentList': [
                'Raju', 'Ramesh', 'Rohan'
            ],
            'studentDetails': [
                {'name': 'Raju', 'mobileNo': '+91 8090602345'},
                {'name': 'Ramesh', 'mobileNo': '+91 8090602350'},
            ],
            'num1': num1,
            'num2': num2,
            'output': result,
        }
        url = "/about_us/?output={}".format(result)
        return HttpResponseRedirect(url)
    except:
        pass

    return render(request, "index.html", data)
    # return render(request, "index.html", {'output':result})

def aboutUs(request):
    output = request.GET.get('output')
    return render(request, "aboutUs.html", {'output': output})

def cars(request):
    return HttpResponse("This page shows cars.")

def carName(request ,carname):
    return HttpResponse(carname)