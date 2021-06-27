from django.shortcuts import redirect, render
from RPList.models import Company, Companyinfo, Jobinformation, Jobrequirements, Jobstatus
from django.views.decorators.csrf import csrf_exempt

def home_page (request):
    companys = Company.objects.all()
    return render (request, 'homepage.html',{'companys' : companys})

def new_item (request):
    companyp_ = Company.objects.create(Ccompanyname = request.POST['Compny'],Aaddress = request.POST['Addres'])
    return redirect (f'/{companyp_.id}/view_list')

def view_list(request,company_id):
    company_ = Company.objects.get(id = company_id)
    #Bbackgroundp = Companyinfo.objects.filter(company = company_id)
    return render(request,'companyinformations.html', {'company':company_})

def add_item(request,company_id):
    company_ = Company.objects.get(id=company_id)
    Companyinfo.objects.create(Bbackground=request.POST['bground'],Ccapabilities=request.POST['capa'],Accreditations=request.POST['accr'],Sstakeholder=request.POST['stake'], company = company_)
    return redirect (f'/{company_.id}/view_list')
def about(request):
    return render(request, 'about.html')


def jobinformations(request):
    return render(request, 'jobinformations.html')

def jobrequirementss(request):
    return render(request, 'jobrequirementss.html')

def jobstatus(request):
    return render(request, 'jobstatus.html')








def edit(request, id):
    companys = Company.objects.get(id=id)
    context = {'companys' : companys}
    return render(request, 'lasts.html',context)

def update(request, id):
    company = Company.objects.get(id=id)
    company.Ccompanyname = request.POST['Compny']
    company.Aaddress = request.POST['Addres']
    company.save()
    return redirect('/')

def delete(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('/')


'''

def homepage(request):
     #company = Company.objects.all()
     return render(request, 'homepage.html')

def companyinformations(request):
     #company = Company.objects.all()
     return render(request, 'companyinformations.html')

def jobinformation(request):
     #company = Company.objects.all()
     return render(request, 'jobinformation.html')

def jobrequirementss(request):
     #company = Company.objects.all()
     return render(request, 'jobrequirementss.html')

def jobstatus(request):
     #company = Company.objects.all()
     return render(request, 'jobstatus.html')

def about(request):
     #company = Company.objects.all()
     return render(request, 'about.html')















def homepage(request):
     company = Company.objects.all()
     return render(request, 'homepage.html',{'company' : company}) 
def new_company(request):
    newcompany_ = homepage.objects.create(Ccompanyname=request.POST['Compny'],Aaddress=request.POST['Addres'],)
    return redirect(f'/{newcompany_.id}/')
def view_Companyinfo(request, Companyinfo_id):   
    Company = Company.objects.get(id=Companyinfo_id):
   return render(request, 'companyinformations.html', {'company': company_}:
def add_item(request,company_id):
    Companyinfo = Company.objects.get(id=company_id) Jobinformation
    return redirect(f'company_id'}/)
    companyinfo_ = companyinformations.objects.get(id=companyinfo_id)    
    companyinformations.objects.create(Bbackground=request.POST['bground'],Ccapabilities=request.POST['capa'],Accreditations=request.POST['accr'], companyinfo=companyinfo_)
     return redirect(f'{company_.id}/')   





def view_list(request,company_id):
    company = Company.objects.get(company_id)
    return render(request,'companyinformations.html') {'Company':company})
def form_list(request):
    return render(request,'homepage.html')
def form_list(request):
    return render(request,'companyinformations.html')
def form_list(request):
    return render(request,'jobinformation.html')
def form_list(request):
    return render(request,'jobrequirements.html')
def form_list(request):
    return render(request,'jobstatus.html')


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
