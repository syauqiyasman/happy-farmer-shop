from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Batang Singkong',
        'price': '1000',
        'description': 'Batang singkong berkualitas, tidak akan tumbuh menjadi jagung.',
        'quantity': '10000',
        'image': 'https://kabarpangan.com/wp-content/uploads/2020/08/23-bibit-IMG20200704141312-678x381.jpg',
    }

    return render(request, "main.html", context)
