"""newpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from new import views#uej


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.validate, name='user'),
    #path('userpage/',views.uservailid,name='userpage')
    path('crud/',views.add_show, name = "addandshow"),
    path('delete/<int:id>/',views.delete_data, name = "deletedata"),
    path('<int:id>/',views.update_data, name = "updatedata"),
    path('crudpri/',views.add_pri, name = "addpri"),
    path('update_pri/<int:id>/',views.update_pri, name = "updatepri"),
    path('deletepri/<int:id>/',views.delete_pri, name = "deletepri"),
    path('check',views.check,name="check")
]

handler404 = 'new.views.error_404'

handler500 = 'new.views.error_500'
