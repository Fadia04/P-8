from django.shortcuts import render
from products.models import Product
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


def home(request):
   # Comment faire une recherche
    """View allowed to return home page"""
    return render(request, "products/home.html")


def product_detail(request, id):
    """View allowed to display products informations in detail page"""
    product = Product.objects.get(id=id)
    return render(request, "products/product_detail.html", {"product": product})


def results(request):
    """View allowed to get the user request filtered by name and displays a list of 6 products in results page"""
    if request.method == "POST":
        query = request.POST["query"]
        products = Product.objects.filter(name__icontains=query).order_by("nutriscore")[
            :6
        ]
        logger.info('New results', exc_info=True, extra={
                    # Optionally pass a request and we'll grab any information we can
                            'request': request,
                                })
        return render(
            request, "products/results.html", {"query": query, "products": products}
        )
    else:
        message = "Nous n'avons pas trouvé le produit recherché, veuillez retaper votre demande"

        return render(request, "products/results.html", {"message": message})

