from django.shortcuts import render
from django.http import HttpResponse
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import django
import markdown2

client = genai.Client(api_key='AIzaSyB-9RSYN1-UrIv_gtnTOwDuDidaTDCUM-s')
# Create your views here.
django.setup()
global var

#function to render home page
def home_view(request):
    return render(request, 'index.html', {} )
    
#result page function
def page2_view(request):
    data = request.POST["userInput"]
    #prompt for generating image
    prompt = f'''You are an art instructor. A student wants to draw '{data}'.
            Provide a very high detailed, step-by-step guide on how to draw it.
            Should be the at least minimum 100 steps with each step beign minimum 3 paragraphs.
            Break down the process into simple, numbered steps.
            For each step, describe the exact lines, shapes, and strokes required.
            Start with the basic outline and progressively add details.
            For example: '1. Start by lightly sketching a large oval in the center of the page for the body.'

            Here are the instructions: also indent it neatly with necessary styles wherever required.
            '''
    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            prompt
        ],
    )
    #markdown to stylie the text
    text=markdown2.markdown(result.text)
    context = {'texts': text}
    return render(request, 'page2.html', context)

#function to render the last page
def last(request):

    return render(request, 'last.html', {})


