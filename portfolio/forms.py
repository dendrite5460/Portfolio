from django import forms 
 
class nameofstock(forms.Form):  
    stockname = forms.CharField(label="Enter name of the stock ",max_length=50,initial='Enter StockName')  

class buy(forms.Form): 
    geeks_field = forms.BooleanField() 
    