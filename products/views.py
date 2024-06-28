from django.shortcuts import render,redirect
from .models import products
from .forms import ProductForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def showallproducts(request):
    product=products.objects.all()

    page_num=request.GET.get("page")

    paginator=Paginator(product, 3)

    try:
        product=paginator.page(page_num)
    except PageNotAnInteger:
        product=paginator.page(1)
    except EmptyPage:
        product=Paginator.page(paginator.num_pages)


    number_of_products = products.objects.all().count()
    print("Total number of products:",number_of_products)  #Total number of products: 5

    context={
        'pro':product,
        'num':number_of_products
             
             }

    return render(request,'showproducts.html',context)
    


# def ShowAllProducts(request):
#     products = Product.objects.all()[1:4]


def details(request, pk):
    eachProduct= products.objects.get(id=pk)


    context = {
        'eachProduct':eachProduct

    }

    return render(request, 'details.html', context)

def addproducts(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showpro')

    context = {
        'form': form
    }

    return render(request, 'addproducts.html',context)


def updateproducts(request,pk):
    product = products.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showpro')

    context = {
        "form_i":form
    }
    return render(request, 'updateproducts.html',context)


def deleteproducts(request, pk):
    product = products.objects.get(id=pk)
    product.delete()
    return redirect('showpro')



def searchbar(request):
    if request.method == 'GET':
        query=request.GET.get('query')    #kalki mahabharatam
        if query:
            product=products.objects.filter(name__icontains=query)

            return render(request, 'searchbar.html',{'pro' : product})
        else:
            print('No Products to Show')
            return render(request,'searchbar.html',{})




