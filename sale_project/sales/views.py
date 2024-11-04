from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Seller, Sale, Product
from .forms import CustomerForm, SellerForm, SaleForm, ProductForm
from django.db.models import Sum
from django.urls import reverse
from django.utils.dateparse import parse_date


def home(request):
    return render(request, 'sales/home.html')


def report(request):
    return render(request, 'sales/report.html')


# Представление для списка покупателей
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'sales/customer_list.html', {'customers': customers})


# Представление для списка продавцов
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'sales/seller_list.html', {'sellers': sellers})


# Представление для списка товаров
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sales/product_list.html', {'products': products})


# Представление для списка продаж
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})


# Представление для добавления покупателя
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Перенаправление на список покупателей
    else:
        form = CustomerForm()
    return render(request, 'sales/add_customer.html', {'form': form})


# Представление для добавления продавца
def add_seller(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')  # Перенаправление на список продавцов
    else:
        form = SellerForm()
    return render(request, 'sales/add_seller.html', {'form': form})


# Представление для добавления товара
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Перенаправление на список товаров
    else:
        form = ProductForm()
    return render(request, 'sales/add_product.html', {'form': form})


# Представление для добавления продажи
def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')  # Перенаправление на список продаж
    else:
        form = SaleForm()
    return render(request, 'sales/add_sale.html', {'form': form})


# Представления для редактирования
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'sales/edit_customer.html', {'form': form})


def edit_seller(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == "POST":
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'sales/edit_seller.html', {'form': form})


def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sales/edit_sale.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'sales/edit_product.html', {'form': form})


# Представления для удаления
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'sales/delete_customer.html', {'customer': customer})


def delete_seller(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == "POST":
        seller.delete()
        return redirect('seller_list')
    return render(request, 'sales/delete_seller.html', {'seller': seller})


def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        sale.delete()
        return redirect('sale_list')
    return render(request, 'sales/delete_sale.html', {'sale': sale})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'sales/delete_product.html', {'product': product})


def customers_by_seller(request, seller_id=None):
    # Если ID продавца передан, отфильтруем покупателей по этому продавцу
    if seller_id:
        customers = Customer.objects.filter(sale__seller_id=seller_id).distinct()
        seller = get_object_or_404(Seller, pk=seller_id)
        return render(request, 'sales/customers_by_seller_report.html', {
            'customers': customers,
            'seller': seller
        })
    # Если ID продавца не передан, отобразим список всех продавцов
    else:
        sellers = Seller.objects.all()
        return render(request, 'sales/select_seller.html', {'sellers': sellers})


def sales_by_date(request, date=None):
    if request.method == "GET" and "date" in request.GET:
        # Извлекаем дату из запроса и перенаправляем на URL отчета с этой датой
        date = request.GET.get("date")
        return redirect(reverse('sales_by_date_report', args=[date]))

    # Если дата передана в URL, отобразим отчет
    if date:
        sales = Sale.objects.filter(date=date)
        return render(request, 'sales/sales_by_date_report.html', {
            'sales': sales,
            'date': parse_date(date)  # Преобразуем строку в формат даты
        })

    # Если ни дата не передана в URL, ни не выбрана в форме, отобразим форму
    return render(request, 'sales/select_date.html')


# def sales_by_date(request, date):
#     sales = Sale.objects.filter(date=date)
#     return render(request, 'sales/sales_by_date.html', {'sales': sales})


def sellers_by_product(request, product_id):
    sellers = Seller.objects.filter(sale__product_id=product_id).distinct()
    return render(request, 'sales/sellers_by_product.html', {'sellers': sellers})


def customers_by_product(request, product_id):
    customers = Customer.objects.filter(sale__product_id=product_id).distinct()
    return render(request, 'sales/customers_by_product.html', {'customers': customers})


def total_sales_by_date(request, date):
    total_sales = Sale.objects.filter(date=date).aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'sales/total_sales_by_date.html', {'total_sales': total_sales})


def top_selling_product(request):
    product = Product.objects.annotate(total_sales=Sum('sale__quantity')).order_by('-total_sales').first()
    return render(request, 'sales/top_selling_product.html', {'product': product})


def top_seller(request):
    seller = Seller.objects.annotate(total_sales=Sum('sale__quantity')).order_by('-total_sales').first()
    return render(request, 'sales/top_seller.html', {'seller': seller})


def top_customer(request):
    customer = Customer.objects.annotate(total_purchases=Sum('sale__quantity')).order_by('-total_purchases').first()
    return render(request, 'sales/top_customer.html', {'customer': customer})


def top_selling_product_in_period(request, start_date, end_date):
    product = Product.objects.filter(sale__date__range=[start_date, end_date]).annotate(total_sales=Sum('sale__quantity')).order_by('-total_sales').first()
    return render(request, 'sales/top_selling_product_in_period.html', {'product': product})


def top_seller_in_period(request, start_date, end_date):
    seller = Seller.objects.filter(sale__date__range=[start_date, end_date]).annotate(total_sales=Sum('sale__quantity')).order_by('-total_sales').first()
    return render(request, 'sales/top_seller_in_period.html', {'seller': seller})


def top_customer_in_period(request, start_date, end_date):
    customer = Customer.objects.filter(sale__date__range=[start_date, end_date]).annotate(total_purchases=Sum('sale__quantity')).order_by('-total_purchases').first()
    return render(request, 'sales/top_customer_in_period.html', {'customer': customer})
