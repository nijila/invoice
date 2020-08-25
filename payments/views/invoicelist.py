from django.shortcuts import render
from finance.models import Invoice
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from urlshortening.models import get_short_url, invalidate_url, get_full_url
from shortener import shortener
import stripe
from users.models import User

@csrf_exempt
def invoicelist(request):
    invoces = Invoice.objects.all()
    return render(request, 'invoicelist.html', locals())

# @csrf_exempt
def sendmail(request):
    
    
    invoice_id=request.POST.get('button')
    invoice = Invoice.objects.get(pk=int(invoice_id))
    domain_url = request.build_absolute_uri().split('api/')[0]
    print(domain_url)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - lets capture the payment later
        # [customer_email] - lets you prefill the email input in the form
        # For full details see https:#stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'name': "Payment",
                    'description': 1,
                    'amount': int(invoice.Amount*100),
                    'currency': 'inr',
                    'quantity': 1
                }
            ]
        )
        
   
        session_id = checkout_session['id']
        link = domain_url+"payment?amount={0}&session_id={1}".format(invoice.Amount, session_id)
        user=User.objects.all().first()
        short_url=domain_url+"s/"+shortener.create(user,link)
        return JsonResponse({'sessionId': checkout_session['id'], 'shortlink':str(short_url)})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    return render(request, 'invoicelist.html', locals())
