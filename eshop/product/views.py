from django.core.paginator import Paginator
from django.shortcuts import render

from product.models import Product, Category
from utils.utils import get_order_count
''' 
arzon qimmat yangi eski
'''
SORTING = {
    'arzon': 'price',
    'qimmat': '-price',
    'yangi': '-id',
    'eski': 'id'

}


def home(request):
    products = Product.objects.all().order_by('-price')[:3]
    return render(
        request=request,
        template_name='index.html',
        context={
            'products': products
        }
    )


def products(request):
    cat = request.GET.get('cat', 0)  # filterlaydigon metod
    page: str = request.GET.get('page', 1)  # paginatorleydigon metod
    per_page: str = request.GET.get('per-page', 6)  # har bir page uchun saralaydigon metod
    sorting: str = request.GET.get('sorting', 'yangi')  # yangi-eski bo'yicha saralaydigon metod
    min_price: str = request.GET.get('min-price', 0)  # yangi-eski bo'yicha saralaydigon metod
    max_price: str = request.GET.get('max-price', 999999999999)  # yangi-eski bo'yicha saralaydigon metod

    if cat:
        product_list = Product.objects.filter(category_id=cat)
    else:
        product_list = Product.objects.all()

    product_list = product_list.filter(price__lte=max_price, price__gte=min_price).order_by(SORTING[sorting])
    category_list = Category.objects.all()

    paginator = Paginator(
        object_list=product_list,
        per_page=per_page
    )
    page = int(page)
    page = int(page) if page <= paginator.num_pages else paginator.num_pages
    product_list_page = paginator.get_page(page)

    badge_count = get_order_count(request)

    return render(
        request=request,
        template_name="product/products.html",
        context={
            'products': product_list_page,
            'categories': category_list,
            'title': 'Mahsulotlar',
            'paginator': paginator,
            'current_page': int(page),
            'current_category': int(cat),
            'sorting': sorting,
            'badge_count': badge_count
        }
    )


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(
        request=request,
        template_name='',
        context={
            'product': product
        }
    )


def search(request):
    search_text = request.GET.get('search', None)  # filterlaydigon metod
    product_list = Product.objects.filter(name__icontains=search_text)
    category_list = Category.objects.all()
    return render(
        request=request,
        template_name="product/products.html",
        context={
            'products': product_list,
            'categories': category_list,
            'title': 'Mahsulotlar'
        }
    )
