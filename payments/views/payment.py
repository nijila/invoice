from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe


def HomePageView(request):
    
    request.session['amount']=request.GET.get('amount')
    request.session['session_id']=request.GET.get('session_id')
    return render(request, 'home.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        print(stripe_config)
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        return JsonResponse({'sessionId': request.session['session_id']})
        