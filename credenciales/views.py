from django.shortcuts import render, redirect
from django.contrib import messages
from credenciales.forms import CredencialesForm


def credenciales_view(request):
    if request.method == 'POST':
        form = CredencialesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Las credenciales se guardaron correctamente.')
            return redirect('credenciales')
    else:
        form = CredencialesForm()
    return render(request, 'credenciales/credenciales.html', {'form': form})

