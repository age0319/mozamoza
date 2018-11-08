from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings

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


def delete(request, num):
    obj = Document.objects.get(id=num)
    obj.delete()
    return redirect('index')


def edit(request, num):

    obj = Document.objects.get(id=num)

    if request.method == 'POST':
        if 'button_gray' in request.POST:
            gray(obj.photo.url)
            obj.gray = "gallery/gray.jpg"
            obj.save()
            return redirect('edit', num)

    params = {'data': obj}

    return render(request, 'edit.html', params)


def gray(url):

    path = settings.BASE_DIR + url

    print(path)
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    output = settings.BASE_DIR + "/media/gallery/gray.jpg"
    cv2.imwrite(output, img_gray)
