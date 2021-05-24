from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Photo
 
 
@require_POST
@csrf_exempt
def receive_image(request):
    upload_file = request.FILES["upload_file"]
    photo = Photo(title="タイトル", image=upload_file)
    photo.save()
    download_url = "http://localhost:3000/" + photo.image.name
    return HttpResponse(download_url, content_type="text/plain")
