from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login_personalizado(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Si es superusuario → va al panel de admin del salón
            if user.is_superuser:
                return redirect('/reservaciones/admin/gestion/')

            return redirect('/reservaciones/admin/consultar/')

        return render(request, "usuarios/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "usuarios/login.html")

