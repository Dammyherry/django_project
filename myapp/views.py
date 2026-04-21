from django.shortcuts import render

def home(request):
    students = [
        {"name": "John", "course": "Math"},
        {"name": "Jane", "course": "Biology"},
        {"name": "Mike", "course": "Computer Science"},
    ]
    return render(request, 'myapp/home.html', {"students": students})