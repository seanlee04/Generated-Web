from django.shortcuts import render
from django.http import HttpResponse
import os
import openai

# Create your views here.

def generate_page(request, url):
    with open("generatedweb/templates/static/prompt.txt", "r") as file:
        prompt = file.read()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": url}
        ],
        max_tokens=3000,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    html = chat_completion.choices[0].message.content
    response = HttpResponse(html, content_type='text/html')
    return response
