
from django.contrib import admin
from django.urls import path , include
from .views import ListUsers, ListItems, getUserCredit, ListCredit, getItemCredit, PaidView,SearchUserCredits
from . import views

urlpatterns = [
    path('api/users/', ListUsers.as_view(), name="list-users"),
    path('api/items/', ListItems.as_view(), name="list-items"),
    path('api/credit/', ListCredit.as_view(), name="list-credits"),
    path('api/item/<int:pk>/', getItemCredit.as_view(), name="list-item-credit"),
    path('api/user/<int:pk>/', getUserCredit.as_view(), name="list-user-credit"),
    path('api/search/',SearchUserCredits.as_view(), name="list-searched-user" ),
    path('items/' ,views.list_users, name="list-items"),
    path('api/paid/', PaidView.as_view(), name="paid"),
    path('<int:pk>/', views.list_user_credit, name="list-user-credit"),
    path('item/<int:pk>/', views.list_item_credit , name="list-credits")


]
