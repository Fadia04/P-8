from unicodedata import name
from django.shortcuts import render
from products.models import Product, Category, Categorized

from itertools import chain

# Create your views here.


def home(request):
    return render(request, "products/home.html")


def product(request):
    products = Product.objects.all()
    return render(request, "products/product.html", {"products": products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "products/product_detail.html", {"product": product})


def results(request):
    if request.method == "POST":
        query = request.POST["query"]
        products = Product.objects.filter(name__icontains=query).order_by("nutriscore")[
            :9
        ]
        # Recherche de la listes des id de produit à l'aide de la tablea categorized       
        #products_pk = []
        #categorie=products.
        #categorie = Category.objects.filter(name__in=products)
        #prod=Categorized.objects.values_list('product_id', flat=True)
        #prod_id=Categorized.objects.filter(product_id=products, category_id=categorie)
        #id=Product.objects.filter(id=prod)       
        #products_pk.append(prod_id)
        #products_filter = Product.objects.filter(pk__in=products_pk).order_by('nutriscore')[:3]
        #all_products = chain(products, products_filter)
        return render(
            request, "products/results.html", {"query": query, "products": products}
        )
    else:
        message = "Nous n'avons pas trouvé le produit recherché"
        return render(request, "products/results.html", {"message": message})


def legal_notices(request):
    return render(
        request,
        "products/legal_notices.html",
    )