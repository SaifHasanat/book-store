from django.urls import path
from .views import PaymentSuccessView, PaymentCheckOutView, PaymentCanceledView

urlpatterns = [

    path('checkout/<uuid:book_id>', PaymentCheckOutView.as_view(), name='checkout'),
    path('success_payment/<uuid:book_id>', PaymentSuccessView.as_view(), name='success_payment'),
    path('canceled_payment/<uuid:book_id>', PaymentCanceledView.as_view(), name='canceled_payment')

]
