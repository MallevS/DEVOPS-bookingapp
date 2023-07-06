from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking


# Create your views here.

@login_required()
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    employees = User.objects.all()

    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        selected_employees = request.POST.getlist('employees')

        booking = Booking(room=room, start_time=start_time, end_time=end_time)
        booking.save()
        booking.user.set(selected_employees)  # Assign selected employees to the booking

        messages.success(request, 'Room booked successfully!')
        return redirect('room_list')

    return render(request, 'book_room.html', {'room': room, 'employees': employees})
