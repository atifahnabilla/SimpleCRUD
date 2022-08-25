from django import forms  
from matkul.models import Matkul 
 
class MatkulForm(forms.ModelForm):  
    class Meta:  
        model = Matkul  
        fields = "__all__"  