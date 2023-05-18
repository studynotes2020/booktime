from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from main import views
from main import models

urlpatterns = [
    path(
        "about-us/",
        TemplateView.as_view(template_name='about_us.html'),
        name="about_us",
    ),
    path(
        "",
        TemplateView.as_view(template_name='home.html'),
        name="home",
    ),
    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name="contact_us",
    ),
    path(
        "products/<slug:tag>/",
        # views.ProductListView.as_view(),
        ListView.as_view(model=models.Product),
        name="products",
    ),
    path(
        "product/<slug:slug>/",
        DetailView.as_view(model=models.Product),
        name="product",
    ),

]
