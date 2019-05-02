"""
This gist allows you to automatically register all models in a given app
for use in the Django Admin application.
Change (your-app-name) to your application name.
Credit : https://gist.github.com/scovetta/3249996
"""

import inspect
from django.contrib.admin.sites import AlreadyRegistered
from . import models
from django.contrib import admin

model_list = [model_info[1] for model_info in inspect.getmembers(models)
              if inspect.isclass(model_info[1])]

for model in model_list:
    try:
        if not model._meta.abstract:
            admin.site.register(model)
    except AlreadyRegistered:
        pass