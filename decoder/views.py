from django.shortcuts import render

# Create your views here.
def decoder_view(request):
    return render(request, 'test/decoder.html')