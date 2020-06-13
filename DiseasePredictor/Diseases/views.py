from django.shortcuts import render

def input_view(request):

    if request.method=="POST":
        return None
    
    return render(request, "input.html",{})
