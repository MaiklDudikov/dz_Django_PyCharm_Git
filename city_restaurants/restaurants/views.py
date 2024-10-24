from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm
from .models import Restaurant


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add_restaurant.html', {'form': form})


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})


def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'restaurants/delete_restaurant.html', {'restaurant': restaurant})


def edit_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/edit_restaurant.html', {'form': form})


def search_restaurants(request):
    query = request.GET.get('query')
    restaurants = Restaurant.objects.filter(specialization__icontains=query) if query else None
    return render(request, 'restaurants/search_restaurants.html', {'restaurants': restaurants, 'query': query})
