from django.shortcuts import render, HttpResponse


def home(request):
    response = {
        "title" : "DevBlog",
        "posts" : [f"Post # {i}" for i in range(1,6)]
    }

    return render(request, "home.html", context=response)


def about(request):
    return HttpResponse("About page")

def post_details(request, pk):
    return HttpResponse("Post Details")
