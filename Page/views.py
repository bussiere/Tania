# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext 
from django.http import HttpResponse 
from pages.models import Page
from scripts_django.tools import recursif_template
from invitation.models import  Invitation


def noteindex(request,logouts=""):
    output = ""
    output += logouts
    if (logouts == 'logout'):
            logout(request)

    try :
        if (request.POST['username'] or request.POST['password']):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    output = accueillog()
                    # Redirect to a success page.
                else:
                    pass
            else:
                output = accueillogvide()
        else :
            output = accueillogvide()
    except :
        if request.user.is_authenticated():
            output = accueillog()
        else :
            output = accueillogvide()
    t = Template(output)
    c = RequestContext(request)
    return HttpResponse(t.render(c))# Create your views here.



def accueillogvide():
    output = """
    <form method="post" action=".">{% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="login" />
    </form>
    """
    return output

def accueillog():
    output = """
    bienvenue<br>
    <a href="../logout/">logout</a>
    """
    return output
