from django.shortcuts import render,redirect
from testapp.models import Player
from testapp.forms import PlayerForm


# Create your views here.
def retrieve_view(request):
    players=Player.objects.all()
    return render(request,'testapp/index.html',{'players':players})

def create_view(request):
    form=PlayerForm()
    if request.method=='POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    player=Player.objects.get(id=id)
    player.delete()
    return redirect('/')

def update_view(request,id):
    player=Player.objects.get(id=id)
    if request.method=="POST":
        form=PlayerForm(request.POST,instance=player)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'player':player})
