from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        print(customer)
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, "orders.html", {'orders': orders})
