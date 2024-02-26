from django.http import JsonResponse
from django.shortcuts import render
from tools import openai_api

openai_key = openai_api.openai_api_key


def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Hello " + message
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbotapp/chatbot.html')
