from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings
import os
from .mosaic import put_mosaic

# Create your views here.


def index(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = DocumentForm()

    params = {
        'form': form
    }

    return render(request, 'index.html', params)


def history(request):
    data = Document.objects.all()

    params = {
        'data': data,
    }

    return render(request, 'history.html', params)


def delete(request, num):
    obj = Document.objects.get(id=num)
    obj.delete()
    return redirect('history')


def edit(request, num):

    obj = Document.objects.get(id=num)

    if request.method == 'POST':
        if 'button_gray' in request.POST:
            file_name = gray(obj.photo.url)
            obj.gray = "gallery/" + file_name
            obj.save()
            return redirect('edit', num)

        elif 'button_mosaic' in request.POST:
            file_name = face_mosaic(obj.photo.url)
            obj.mosaic = "gallery/" + file_name
            obj.save()
            return redirect('edit', num)

    params = {'data': obj}

    return render(request, 'edit.html', params)


def face_mosaic(url):

    # カスケードファイルを指定して検出器を作成
    cascade_file = settings.BASE_DIR + "/static/xml/" + "haarcascade_frontalface_alt.xml"

    cascade = cv2.CascadeClassifier(cascade_file)

    ## 元のファイル名に_mosaicを付け足す
    path = settings.BASE_DIR + url

    # splitextで、拡張子とそれ以外を分離する
    # /Users/haru/PycharmProjects/opencv/mosaic_app/media/gallery/DSC_1284
    file = os.path.splitext(path)[0]

    # .jpg
    ext = os.path.splitext(path)[1]

    output = file + "_mosaic" + ext

    # basenameで、ファイル名を取り出す
    # DSC_1284_mosaic.jpg
    mosaic_file = os.path.basename(output)

    # 画像を読み込んでグレイスケールに変換する
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔認識を実行
    face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))

    # 結果を確認
    if len(face_list) == 0:
        print("失敗")
        # quit()

    # 認識した部分に印をつける
    for (x, y, w, h) in face_list:
        img = put_mosaic(img, (x, y, x + w, y + h))

    # 画像を出力
    cv2.imwrite(output, img)

    return mosaic_file


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
