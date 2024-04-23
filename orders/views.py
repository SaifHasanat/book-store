from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.shortcuts import get_object_or_404, render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from books.models import Book
import uuid, logging


class PaymentSuccessView(TemplateView):
    template_name = 'orders/success_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        context['book'] = book
        return context


class PaymentCanceledView(TemplateView):
    template_name = 'orders/canceled_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        context['book'] = book
        return context

class PaymentCheckOutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = PayPalPaymentsForm

    def get_initial(self, **kwargs):
        book_id = self.kwargs.get('book_id')
        self.book = get_object_or_404(Book, id=book_id)
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': str(self.book.price),
            'currency_code': 'USD',
            'item_name': str(self.book.title),
            'invoice': uuid.uuid4(),
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': self.request.build_absolute_uri(reverse('success_payment',kwargs={'book_id':self.book.id})),
            'cancel_return': self.request.build_absolute_uri(reverse('canceled_payment',kwargs={'book_id':self.book.id})),
            'cmd': '_xclick',
            'lc': 'EN',
            'no_shipping': '1',
        }
        return paypal_dict

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.book
        return context


logger = logging.getLogger(__name__)


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            return
        try:
            transaction_pk = ipn_obj.invoice
            mytransaction = MyTransaction.objects.get(pk=transaction_pk)
            assert ipn_obj.mc_gross == mytransaction.amount and ipn_obj.mc_currency == mytransaction.currency

        except MyTransaction.DoesNotExist:
            logger.exception('Transaction does not exist.')
        except Exception:
            logger.exception('Payment data does not match transaction data.')
        else:
            mytransaction.paid = True
            mytransaction.save()
    else:
        logger.debug(f'Paypal payment status not completed:{ipn_obj.invoice}')


