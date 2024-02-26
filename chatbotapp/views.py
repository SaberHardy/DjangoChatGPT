import openai
from django.http import JsonResponse
from django.shortcuts import render
from tools import openai_api

openai_key = openai_api.openai_api_key
openai.api_key = openai_key


def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbotapp/chatbot.html')


def ask_openai(message):
    response = openai.completions.create(
        model='gpt-3.5-turbo',
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()

    return answer
