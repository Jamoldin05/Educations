from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import logout,login




def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('upskill:index')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})



def logout_view(request):
    logout(request)  
    return redirect('upskill:index')