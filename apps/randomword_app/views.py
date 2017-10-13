from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
    try:
        request.session['count']
    except:
        request.session['count']=0
    return render(request, 'randomword_app/index.html',)

def generate(request):
    if request.method == "POST":
        word=""
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(0,14):
            letterindex=randint(0,len(letters)-1)
            word += letters[letterindex]
        
        request.session['count']=request.session['count']+1
        request.session['word']=word
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['count']=0
        request.session['word']=""
        return redirect('/')
    else:
        return redirect('/')
