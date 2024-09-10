from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'products': [
            {
                'name': 'Batang Singkong',
                'price': '1000',
                'description': 'Batang singkong berkualitas, tidak akan tumbuh menjadi jagung.',
                'quantity': '10000',
                'image': 'https://cdn.syauqiyasman.com/static/image/batang-singkong.webp',
            },
            {
                'name': 'Susu Ikan',
                'price': '7500',
                'description': 'Susu ikan, dapat digunakan untuk memenuhi gizi anak bangsa.',
                'quantity': '1000',
                'image': 'https://cdn.syauqiyasman.com/static/image/susu-ikan.webp',
            },
            {
                'name': 'Sawit Papua',
                'price': '10000',
                'description': 'Sawit Papua, produk ini berpotensi menyebabkan krisis iklim.',
                'quantity': '100000',
                'image': 'https://cdn.syauqiyasman.com/static/image/sawit-papua.webp',
            },
        ]
    }

    return render(request, "main.html", context)
