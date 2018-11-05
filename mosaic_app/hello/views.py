from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document

# Create your views here.


def index(request):
    data = Document.objects.all()
    params = {'data': data}
    return render(request, 'index.html', params)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
