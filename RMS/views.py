from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import createProForm, createEmpForm, searchEmpForm, searchProForm, createDepForm, TransactionsForm, signupform, loginform
from .models import products, employees, transactions, department
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import date, datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')

def Base(request):
    return render(request, 'Basic.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if (request.method=='POST'):
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            
            
            # try:
            #     e=employees.objects.get(EmpID=int(username))
            #     print(e)
            #     login(request, user)
            #     e.theUser= request.user
            # except:
            #     return render(request,'errorid.html')
            
            return redirect('/home')


            # first_name= form.cleaned_data['first_name']
            # last_name= form.cleaned_data['last_name']
            # email= form.cleaned_data['email']
            # username= form.cleaned_data['username']
            # password= form.cleaned_data['password']

        else:
            messages.error(request, "Data seems invalid")
            return render(request,'signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
        
        
        # user= User.objects.create_user(first_name= first_name, last_name=last_name, username=username, email=email, password=password)
        # user.save()
        # messages.success(request, "Account created Successfully !")
        # return redirect('/login')
    
    # else:
    #     form= UserCreationForm()
    
    # return render(request, 'signup.html', {'form':form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})



#   THESE ARE ALSO MUST SEEEE---- COMMENTING TO TEST OTHER CODE......
# def loginview(request):
#     if (request.method=='POST'):
#         form= loginform(request.POST)
#         if(form.is_valid()):
#             username= form.cleaned_data['username']
#             password= form.cleaned_data['password']

#         user=authenticate(username=username, password=password)
#         login(request, user)
#         messages.success(request, 'successfully logged in')
#         return redirect('/home')
    
#     else:
#         form= loginform()
#         return render(request, 'login.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('/signin/')

def emppro(request):
    e= employees.objects.get(user=request.user)
    a= transactions.objects.filter( officeID__Name = e.Name)
    return render(request, 'emppro.html', {'a': a })

def createpro(request):
    if request.method=='POST':
        form = createProForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            category = form.cleaned_data['Category']
            quantity = form.cleaned_data['Quantity']
            company = form.cleaned_data['Company']
            addedOn = date.today()

        p= products.objects.create(Name=name, Category=category, addedOn=addedOn, Quantity=quantity, Company=company)
        p.save()

    #else:
    form = createProForm()

    return render(request, 'createPro.html', {'form': form})

def createemp(request):
    if request.method=='POST':
        form = createEmpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            depart = form.cleaned_data['Department']
            empID = form.cleaned_data['EmpID']
            
        e= employees.objects.create(Name=name, Department=department.objects.get(Name= depart), EmpID=empID)
        e.save()

    else:
        form = createEmpForm()

    return render(request, 'createEmp.html', {'form': form})


def createdep(request):
    if request.method=='POST':
        form = createDepForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            empcount = form.cleaned_data['empcount']
            
        e= department.objects.create(Name=name, empcount=empcount)
        e.save()

    #else:
    form = createDepForm()

    return render(request, 'createdep.html', {'form': form})


def viewEmpList(request):
    if request.method=='POST':
        form = searchEmpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data.get('Name')
            depart = form.cleaned_data.get('Department')
            d= e= employees.objects.all()
            if( name != 'All'):
                e= employees.objects.filter(Name=name)
            if(depart != 'All'):
                d= employees.objects.filter(Department__Name=depart)
            
            e= [ i for i in e if i in d]
            # if(name==depart):
            #     e= employees.objects.all()
    else:
        form = searchEmpForm()
        e= employees.objects.all()
        u= User.objects.all()
 # c=0
    # for i in u:
    #     if(c<3):
    #         c+=1
    #         continue
    #     print(i.username, employees.objects.get(user=i))
    context= {'form':form,
                'e' : e,
                   }
    return render(request, 'viewEmpList.html', context=context)

def viewProList(request):
    if request.method=='POST':
        form = searchProForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            category = form.cleaned_data['Category']
            company = form.cleaned_data['Company']
            
            p= products.objects.all()
            if( name != 'Show All Data'):
                n= products.objects.filter(Name=name)
            else: n=products.objects.all()

            if(category != 'Show All Data'):
                c= products.objects.filter(Category=category)
            else: c=products.objects.all()

            if(company != 'Show All Data'):
                co= products.objects.filter(Company=company)
            else: co=products.objects.all()

            p= [ i for i in p if i in n if i in c if i in co]
            
    else:
        form = searchProForm()
        p= products.objects.all()
    
    context= {'form':form,
                'p' : p    }
    return render(request, 'viewProList.html', context=context)

def viewTransactionList(request):
    if request.method=='POST':
        form = TransactionsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            oid = form.cleaned_data['officeID']
            pid = form.cleaned_data['proID']
            isu= date.today()
            quan = form.cleaned_data['quantity']

            transactions.objects.create( officeID=oid,proID=pid, issueDate=isu, quantity=quan )
    else:
        form = TransactionsForm()
    t= transactions.objects.all()
    
    context= {'form':form,
                't' : t    }
    return render(request, 'viewTransactionList.html', context=context)
