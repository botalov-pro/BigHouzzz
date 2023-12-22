# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0038297/data/www/bh.botalov.pro/BigHouzzz')
sys.path.insert(1, '/var/www/u0038297/data/bh_django_env/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'BigHouzzz.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()