from django.shortcuts import render
from .forms import reservationform

# Create your views here.

def reserve(request):
    reserve_form = reservationform()
    if request.method == "POST":
        reserve_form = reservationform(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = reservationform()

    context = {
        "form" : reserve_form
    }

    return render(request,"reservation/reservation.html",context)