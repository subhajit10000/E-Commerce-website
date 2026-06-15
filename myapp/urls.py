from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index-page'),
    path('', views.index, name='index-page'),
    path('product', views.product, name='product-page'),
    path('contact', views.contact, name='contact-page'),
    path('reg/', views.userReg, name='reg-page'),
    path('login/', views.userLog, name='log-page'),
    path('logout/', views.userLogout, name='log-out-page'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.view_cart, name='view_cart'),
    path('remove/<int:id>', views.remove_cart, name='remove_cart'),
    path('cat_product/<int:id>', views.cat_product, name='cat_product-page'),
    path("initiate-payment/", views.initiate_payment, name="initiate_payment"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-failed/", views.payment_failed, name="payment_failed"),
    path("myorder/", views.myOrders, name="my-orders"),
    path('smartphones',views.smartphones,name='smartphones-page'),
    path('home_appliances',views.home_appliances,name='home_appliances-page'),
    path('camera',views.camera,name='camera-page'),
    path('other_electronic_gadget',views.other_electronic_gadget,name='other_electronic_gadget-page'),
    path('iot_components',views.iot_components,name='iot_components-page'),
    path('laps_tab',views.laps_tab,name='laps_tab-page'),
    path('watch',views.watch,name='watch-page'),


]
