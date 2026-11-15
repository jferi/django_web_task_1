from django.shortcuts import render,redirect
from .models import Program,Velemeny
from .forms import VelemenyForm

def index(request):
    return render(request, 'index.html')

def programok(request):
    programok = Program.objects.all()
    return render(request, 'programok.html', {'programok': programok})

def velemenyek(request):
    velemenyek = Velemeny.objects.all()
    if request.method == 'POST':
        form=VelemenyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('velemenyek')
    else:
        form=VelemenyForm()
    return render(request, 'velemenyek.html', {'velemenyek': velemenyek,'form':form})

def kapcsolat(request):
    return render(request, 'kapcsolat.html')
