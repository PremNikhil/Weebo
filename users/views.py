from django.shortcuts import redirect, render, redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm



def Register(request):
    if request.method == 'POST' :
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konnichiwa {username}!, Your account has been created. You can now login.')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def Profile(request):
    if request.method == 'POST' :
      UU_form = UserUpdateForm(request.POST, instance=request.user)
      PU_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      if UU_form.is_valid() and PU_form.is_valid():
          UU_form.save()
          PU_form.save()
          messages.success(request, f'Yatta!, Your account has been updated.')
          return redirect('Profile')
    else:
      UU_form = UserUpdateForm(instance=request.user)
      PU_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'UU_form': UU_form,
        'PU_form': PU_form
    }
    return render(request, 'users/profile.html', context)


    

  