from django.shortcuts import render, redirect
from .models import Room, Messange
from django.http import HttpResponse, JsonResponse

# Create your views here.


def Home(request):
    return render(request, 'app/home.html')

def RooM(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {'username':username, 'room':room, 'room_details':room_details}
    return render(request, 'app/room.html', context)

def Checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def Send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Messange.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message send successfully')
    
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    
    messages = Messange.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})