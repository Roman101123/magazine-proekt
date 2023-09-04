from django.shortcuts import render

from shop.models import tech

from django.contrib.auth.models import User

from django.contrib.auth import authenticate


from django.http import HttpResponse

# Create your views here.

def index(request):
    new = tech.objects.all()
    if request.method == "POST":
        data = request.POST
        new = tech.objects.filter(category = data["sr"])
        
    return render(request, "index.html", {"new":new})


def card(request, techid):
    new = tech.objects.filter(id = techid)
    return render(request, "card.html", {"new":new})



def reg(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new_user = User.objects.create_user(data["lgn"], data["eml"], data["psw"])
        new_user.save()
        return HttpResponse(f"Поздравляю, {data['lgn']}, вы успешно прошли регистрацию")
    else:
      return render(request, "register.html")
    



def auth(request):
    if request.method == "POST":
        data = request.POST

        user = authenticate(username = data["lgn"], password = data["psw"])
        if user is not None:
            return HttpResponse(f"Привет, {user}, рад тебя видеть")
        else:
            return HttpResponse("Вы ошиблись при вводе данных")
    else:
      return render(request,"auth.html")
