from django.shortcuts import render, redirect  
from matkul.forms import MatkulForm  
from matkul.models import Matkul  

# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = MatkulForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/read')  
            except:  
                pass  
    else:  
        form = MatkulForm()  
    return render(request,'index.html',{'form':form})  

def read(request):  
    matkuls = Matkul.objects.all()  
    return render(request,"read.html",{'matkuls':matkuls})  

def update(request, id):  
    matkul = Matkul.objects.get(id=id)  
    return render(request,'update.html', {'matkul':matkul})  

def update_matkul(request, id):  
    matkul = Matkul.objects.get(id=id)  
    form = MatkulForm(request.POST, instance = matkul)  
    if form.is_valid():  
        form.save()  
        return redirect("/read")  
    return render(request, 'update.html', {'matkul': matkul})  

def delete(request, id):  
    matkul = Matkul.objects.get(id=id)  
    matkul.delete()  
    return redirect("/read")