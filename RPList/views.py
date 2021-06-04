from django.shortcuts import render, redirect
from django.http import HttpResponse
from RPList.models import Company, Companyinfo

def home_page(request):
    companyinfos=Company.objects.all()
    return render(request, 'homepage.html',{ 'companyinfos' : companyinfos })
        
def view_list(request, company_id):
    company_= Company.objects.get(id=company_id)
    return render(request,'complaint.html',{ 'company' : company_ })
    
def  new_list(request):
    company_= Company.objects.create()
    #Companyinfo.objects.create(Ccompanyname=request.POST['Jollibee'],Aaddress=request.POST['Bucandala 3,Imus Cavite'] company=company_)    
    return redirect(f'/RPList/{company_.id}/')
    
def add_item(request, company_id):
    company_=Company.objects.get(id=company_id)
    #Companyinfo.objects.create(Bbackground=request.POST['Bbackground'],Ccapabilities=request.POST['Ccapabilities'],Accreditations=request.POST['Accreditations'],Accreditations=request.POST['Accreditations'],Sstakeholders=request.POST['Sstakeholders']  company=company_)
    return redirect(f'/RPList/{company_.id}')
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


































