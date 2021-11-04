from django.urls import path

from apps.hi.views import say_hello, say_my_name, readiness, liveness

urlpatterns = [
    path('say_hello/', say_hello),
    path('say_my_name/', say_my_name),
    path('readiness/', readiness),
#     path('healthz/', liveness),
]
