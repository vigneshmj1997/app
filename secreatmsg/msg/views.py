from django.shortcuts import render
from django.http import HttpResponse 
import pyrebase


firebase = pyrebase.initialize_app(config)
db=firebase.database()
def home(req,user_name):
    
    if(req.method=="POST"):
        if(db.child(user_name).get.val()!=None):
            db.child(user_name).child("message").push(req.POST.dict()["message"])
            return render(req,"template/create.html",{})
        else:
            return HttpResponse("this Link doenst exist")    
    elif(req.method=="GET"):    
        
        return render(req,"template/home.html",{})



def name(req):
    if(req.method=='POST'):
        val=req.POST.dict()
        string=val["name"]+val["pass"]
        print("&&&&&&&&&&&&&")
        if(db.child(val["name"]).child("pass").get().val()!=None):
            return render(req,"template/form.html",{"waring":"Already exist"})    
            
        db.child(val["name"]).child("pass").set({"pass":val["pass"]})
        db.child(val["name"]).child("message").set({"ano":"msg"})
        return HttpResponse(string)

    else:
        return render(req,"template/form.html",{"waring":""})    

def olala(req,user_name,password):
    if(db.child(user_name).child("pass").get().val()["pass"]==str(password)):
        print(db.child(user_name).child("message").get().val())
        return render(req,"template/message.html",{"val":db.child(user_name).child("message").get().val().values()})       
    else:
        return HttpResponse("<h1>Line doest Exist</h1>")           