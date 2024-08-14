from django.shortcuts import render
import requests
def index(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNmM1ZDRkZmUxNzhhNzI4OTk2NWQzMzkxODE3NWY0YyIsIm5iZiI6MTcyMzU0MTMwMC43MjQwNTQsInN1YiI6IjY2YjllNWQ0ODM0YzNkMGM1NWI3NjBiNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FWc4MQVoxQCHNytKC-rRri2qtXKZQfOHOiKpdSMGk40"
    }

    response = requests.get(url, headers=headers)
    posts = response.json()
    data = posts['results']
    context = {
        "data":data
    }

    return render(request, "youtube.html",context)
