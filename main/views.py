from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Zufar Romli Amri',
        'kelas': 'PBP D',
    }

    return render(request, "main.html", context)