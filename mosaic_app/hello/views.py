from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings
import os

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
            file_name = gray(obj.photo.url)
            obj.gray = "gallery/" + file_name
            obj.save()
            return redirect('edit', num)

    params = {'data': obj}

    return render(request, 'edit.html', params)


def gray(url):

    path = settings.BASE_DIR + url

    # /Users/haru/PycharmProjects/opencv/mosaic_app/media/gallery/DSC_1284
    file = os.path.splitext(path)[0]
    # .jpg
    ext = os.path.splitext(path)[1]

    output = file + "_gray" + ext

    # DSC_1284_gray.jpg
    gray_file = os.path.basename(output)

    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output, img_gray)

    return gray_file
