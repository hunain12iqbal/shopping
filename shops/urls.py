from django.urls import path
from .import views


urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="tracking"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.productView , name="prodview"),
    path("checkout",views.checkout,name="checkout"),





]