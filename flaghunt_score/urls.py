from django.urls import path
from . import views

urlpatterns = [
  path("",views.index.as_view(),name="index") # クラスベースの場合は as_view メソッドを呼び出す
]