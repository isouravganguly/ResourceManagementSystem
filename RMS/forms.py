from django import forms
from django.forms import ModelForm, widgets
from .models import department, products, employees, transactions
from django.forms import Textarea
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
e=employees.objects.all()
d=department.objects.all()
OPTIONne= [tuple([x.Name,x.Name]) for x in e]
OPTIONd= [tuple([x.Name,x.Name]) for x in d]
p=products.objects.all()
OPTIONnp= [tuple([x.Name,x.Name]) for x in p]
OPTIONc= [tuple([x.Category,x.Category]) for x in p]
OPTIONco= [tuple([x.Company,x.Company]) for x in p]

class loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class signupform(forms.Form):
    username = forms.CharField(max_length=20)
    first_name= forms.CharField(max_length=20)
    last_name= forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    email= forms.EmailField(max_length=50)

class createProForm(ModelForm):
    class Meta:
        model = products
        fields = ['Name', 'Category', 'Quantity', 'Company']

class createEmpForm(ModelForm):
    class Meta:
        model = employees
        fields = ['Name','Department','EmpID']

class createDepForm(ModelForm):
    class Meta:
        model = department
        fields = ['Name','empcount']

class searchEmpForm(forms.Form):
    Name= forms.ChoiceField(choices=OPTIONne)
    Department= forms.ChoiceField(choices=OPTIONd)
    # class Meta:
    #     model= employees
    #     fields= ['Name','Department']
    #     widgets = {
    #         "Name": Textarea(
    #             attrs={
    #                 "placeholder": "Show All",
    #                 'required':False,
    #                 'initial': 'Show All'
    #             }
    #         )
    #     }

class searchProForm(forms.Form):

    Name= forms.CharField(label='Product Name:', widget=forms.Select(choices=OPTIONnp))
    Category= forms.CharField(label='Product category:', widget=forms.Select(choices=OPTIONc))
    Company= forms.CharField(label='Product company:', widget=forms.Select(choices=OPTIONco))
    
class TransactionsForm(ModelForm):
    class Meta:
        model = transactions
        fields = ['officeID','proID','quantity']
        # widgets = {
        #     "officeID": 'Select Employee: ',
        #     'productID': 'Select Product: ',
        #     'quantity': 'Select Quantity: '
        # }


