from django.shortcuts import redirect, render

# Create your views here.
from .forms import ImageForm
from .models import Image


def index(request):
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ImageForm()
    
    return render(request ,'index.html' , {'images' : images , 'form': form})