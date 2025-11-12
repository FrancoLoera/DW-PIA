from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def login_personalizado(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/reservaciones/admin/gestion/')
            else:
                return redirect('/reservaciones/empleado/gestion/')

        return render(request, "usuarios/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "usuarios/login.html")


def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # te manda al menú principal
