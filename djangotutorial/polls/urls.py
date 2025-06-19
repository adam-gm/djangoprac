from django.urls import path
from . import views

# When reaching this url through the web browser, the HttpResponse from views.index will be sent to the web page.
# "" in path indicates that the url stops at 127.0.0.1:8000/polls/
urlpatterns = [
    path("", views.index, name="index")
]