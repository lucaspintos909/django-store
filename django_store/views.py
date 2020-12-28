from django.shortcuts import render

def index(request):

    products=[ # ESTO ES PARA PRUEBAS, QUITAR AL INCLUIR BD
            {'title': 'Camiseta', 'price' : 750, 'stock': True},
            {'title': 'Buzo', 'price' : 1500, 'stock': True},
            {'title': 'Crocks', 'price' : 1200, 'stock': False},
            {'title': 'Campera', 'price' : 1340, 'stock': True},
            {'title': 'Gorro de lana', 'price' : 800, 'stock': False}
    ]

    context= {
        'title': 'Django Store',
        'text_button': 'Prueba',
        'products': products
        
    }

    return render(request, 'index.html', context)