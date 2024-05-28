from django.shortcuts import render,redirect
from . models import Skills, Education, Exprience, Cvprofile, Projects, Information, MainPic, ContactMsg, Presentation
from . forms import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'GET' :
        skill = Skills.objects.all()
        education = Education.objects.all()
        exprience = Exprience.objects.all()
        cvprofile = Cvprofile.objects.first()
        project = Projects.objects.all()
        info = Information.objects.first()
        mainpic = MainPic.objects.last()

        context = {
            'skill': skill,
            'education' : education,
            'exprience' : exprience,
            'cvprofile' : cvprofile,
            'project': project,
            'info' : info,
            'mainpic': mainpic
        }
        return render (request, 'home/index.html',context)
    elif request.method == 'POST':
        contactform = Contact(request.POST)
        if contactform.is_valid():
            n = contactform.cleaned_data.get('name')
            e = contactform.cleaned_data.get('email')
            p = contactform.cleaned_data.get('phone')
            m = contactform.cleaned_data.get('msg')
            msgfinal = ContactMsg(name = n , email = e , phone = p , msg = m)
            msgfinal.save()
            messages.success(request,'Your message has been successfully sent. Please click on the message to view it and make it disappear.')
            return redirect('/')
        

def presentations(request):
    p = Presentation.objects.all()
    return render(request, 'home/presentations.html', {'pre': p})