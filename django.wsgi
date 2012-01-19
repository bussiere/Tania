import os, sys  
  
  
sys.path.append('C:/Dropbox/')  
  
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'Tania.settings'  
  
  
import django.core.handlers.wsgi  
  
  
application = django.core.handlers.wsgi.WSGIHandler()  