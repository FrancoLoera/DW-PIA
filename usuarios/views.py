from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login_personalizado(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # inicia sesión
            # redirección según tipo
            if user.is_superuser:
                return redirect('gestion_admin')
            elif user.is_staff:
                return redirect('gestion_empleado')
            else:
                return redirect('index')
        else:
            return render(request, "usuarios/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "usuarios/login.html")

