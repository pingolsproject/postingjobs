from django.shortcuts import render, redirect
from django.http import HttpResponse
from RPList.models import Company, Companyinfo, Jobinformation, Jobrequirements, Jobstatus

def home_page(request):
    companyinfo=Companyinfo.objects.all()
    return render(request, 'homepage.html',{'companyinfo':companyinfo})
        
    
def  job1(request):
    return render(request, 'companyinformations.html')
    
def job2(request):
    return render(request, 'jobinformations.html')

def job3(request):
    return render(request, 'jobrequirementss.html')

def job4(request):
    return render(request, 'jobstatus.html')

def about(request):
    return render(request, 'about.html')


    




'''
def Datamanipulation(request):
   
    company = Company(Compny="Rose Company")
    company.save()
 
    company = Company.objects.all()
    result = 'Printing all company: <br>'
    for x in objects:
        res == x.Ccompanyname+"<br>"    
    companyname = Company.objects.get(id="company")   
    res += 'Printing One entry <br>'
    res += companyname.Ccompanyname
      
    res += '<br> Deleting an entry <br>'
    companyname.delete()
    
    company = Company.objects.get(Compny = 'Rose Company')
    company.Aaddress = "Manila"
    company.save()
    res = ""
    qs = Companyinfo.objects.filter(Bbackground = "Established 2020")
    res += "Found: %s results<br>"%len(qs)
    
    qs = Company.objects.order_by("Aaddress")
    for x in qs:
        res += x.Ccompanyname + x.Aaddress +'<br>'
        '''


































