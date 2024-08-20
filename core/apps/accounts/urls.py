from django.urls import path
from .views import view ,view2,view3
urlpatterns = [
    path('view1/',view,name='view1'),
    path('view2/<int:id>/',view2,name='view2'),
    path('view2/<int:id>/<str:name>/',view3,name='view3'),
]