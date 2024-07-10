from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ElimuApp.urls')),
]

# Static folder
# Images,icons,files etc will be added to this directory:
# Once created on the root folder,register it in the settings,as follows:
# STATICFILES_DIRS = [
    # BASE_DIR, 'static'
# ]
# Create a style sheet under another folder eg css
# call the stylesheet on the respective file,index