from django.shortcuts import render

# Create your views here.
def student_index(request):
    return render(request, "students/index.html")

