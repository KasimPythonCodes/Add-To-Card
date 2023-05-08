from django.shortcuts import render ,redirect
from app.models import Cart ,Product
from django.contrib.auth.models import User

# Create your views here.
def Product_add(request):
    if request.method == 'POST':
        user =request.user.id
        pro_image = request.FILES.get('pro_image')
        dicount_price = request.POST.get('dicount_price')
        user_id = User.objects.get(id=user)
        obj = Product(product_image=pro_image ,dicount_price=dicount_price ,user=user_id)
        obj.save()
    pro = Product.objects.all()  
    user = request.user
    card = Cart.objects.filter(usercart = user) 
    count=card.count()
    return render(request, 'home.html' ,{'pro':pro ,'card':card,'count':count })    


def Add_To_Card(request):
    count =0
    user =request.user
    prod_id = request.GET.get('prod_id')
    prod_id_id = Product.objects.get(id=prod_id)
    Cart(usercart = user , product=prod_id_id).save()
    return redirect('/') 


def Delete_Card(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(Product_add)    
    

