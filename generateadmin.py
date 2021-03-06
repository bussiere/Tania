import sys

prjname = "Matagot"
import os
appname ="tag"
os.environ['DJANGO_SETTINGS_MODULE'] = prjname + '.settings'

exec "from %s.%s import models" % (prjname,appname)

fp = open("%s/%s/admin.py" % (prjname,appname), "w")

print >> fp,  '''#coding: utf-8
from django.contrib import admin
from %s.%s.models import *
''' % (prjname,appname)

for name, klazz in models.__dict__.items():
    if isinstance(klazz, type) and issubclass(klazz, models.models.Model):
        #print name, klazz
        if hasattr(klazz, 'Admin'):
            print >> fp,  'class %sAdmin(admin.ModelAdmin):' % name
            #print dir(klazz.Admin)
            attrs = [(k, v) for k, v in klazz.Admin.__dict__.items() if k[0] != '_']
            if len(attrs):
                for k, v in attrs:
                    if k=='fields':
                        k = 'fieldsets'
                    print >> fp, "\t%s=%s" % (k, repr(v).encode('utf-8'))
            else:
                print >> fp, "\tpass"
            print >> fp, "admin.site.register(%s, %sAdmin)" % (name, name)
            print >> fp
