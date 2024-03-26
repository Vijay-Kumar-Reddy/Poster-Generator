from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt


from . utils import embed_QR

import base64


def choose (request):
    return render(request,'home/choose.html')


@csrf_exempt
def generate (request,style):
    s = style.split('-')
    branch=s[0]
    template = s[1]
    if request.method=="POST":
        U_name = request.POST['U_name']
        O_by = request.POST['O_by']
        E_name = request.POST['E_name']
        Time = request.POST['Time']
        Date= request.POST['Date']
        Venue = request.POST['Venue']
        Faculty = request.POST['Faculty']
        Student = request.POST['Student']
        Link = request.POST['Link']

        #qrcode
        url = Link
        name = "qrcode"+".png"
        embed_QR(url,name)
        with open(name, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        

        list =['sathyabama university','sathyabama institute of science and technology','sist','sathyabama']
        key=''
        if 'sathyabama' in U_name.lower() or U_name.lower() == 'sist':
            key = 'clg'
        

        my_dict = {
            'key':key,
            'U_name' :U_name,
            'O_by' :O_by,
            'E_name' : E_name,
            'Time' :Time,
            'Date' : Date,
            'Venue' : Venue,
            'Faculty' : Faculty,
            'Student' : Student,
            'Link' : Link,
            'image':image_data,
        }
        
        goto = 'home'+'/'+branch+'/'+template+'/'+template+'.html'
        return render(request,goto,my_dict)
    load_page ='home'+'/'+branch+'/'+template+'/'+template+'_f.html'
    return render(request,load_page)
    


def cse_template_4 (request):
    if request.method=="POST":
        U_name = request.POST['U_name']
        O_by = request.POST['O_by']
        E_name = request.POST['E_name']
        Time = request.POST['Time']
        Day= request.POST['Day']
        Month= request.POST['Month']
        Year= request.POST['Year']
        Venue = request.POST['Venue']
        Faculty = request.POST['Faculty']
        Student = request.POST['Student']
        Link = request.POST['Link']

        #qrcode
        url = Link
        name = "qrcode"+".png"
        embed_QR(url,name)
        with open(name, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        

        list =['sathyabama university','sathyabama institute of science and technology','sist','sathyabama']
        key=''
        if 'sathyabama' in U_name.lower() or U_name.lower() == 'sist':
            key = 'clg'
        

        my_dict = {
            'key':key,
            'U_name' :U_name,
            'O_by' :O_by,
            'E_name' : E_name,
            'Time' :Time,
            'Day':Day,
            'Month':Month,
            'Year':Year,
            'Venue' : Venue,
            'Faculty' : Faculty,
            'Student' : Student,
            'Link' : Link,
            'image':image_data,
        }
        
        # goto = 'home'+'/'+branch+'/'+template+'/'+template+'.html'
        goto='home/cse/template4/template4.html'
        return render(request,goto,my_dict)
    # load_page ='home'+'/'+branch+'/'+template+'/'+template+'_f.html'
    load_page='home/cse/template4/template4_f.html'
    return render(request,load_page)
