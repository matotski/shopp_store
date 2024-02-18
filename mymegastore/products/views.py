from django.shortcuts import render

def index(request):
    context = {
        'title' : 'myramasa666'
    }
    return render(request, 'index.html', context = context)


def products(request):
    context = {
        'title' : 'myramasa666',
        'products' : [
            {'img' : '/static/vendor/img/products/Blue-jacket-The-North-Face.png' ,
             'name' : 'Синяя куртка The North Face',
             'price' : '23 725,00 руб.',
             'desc' : 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},

            {'img': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.'},

            {'img': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'desc': 'Плотная ткань. Легкий материал.'},

            {'img': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'desc': 'Гладкий кожаный верх. Натуральный материал.'},

            {'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},

            {'img': '/static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},


        ]
    }
    return render(request, 'products.html', context = context)
