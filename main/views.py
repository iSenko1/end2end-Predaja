from django.shortcuts import render, redirect
from .models import Zaposlenici, Odjeli
from .forms import ZaposleniciForm
from datetime import datetime
from django.urls import reverse


# Create your views here.

def home(request):

    return render(request, "main/home.html")


def summary(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    odjel_svi = Odjeli.objects.all()
    zaposlenici = Zaposlenici.objects.filter(odjel__odjeli_org__icontains=q).order_by('odjel', 'prezime')

    zap_sum = Zaposlenici.objects.all()
    sum_odjel = zap_sum.count()

    context = {
        "zaposlenici": zaposlenici,
        "odjel_svi": odjel_svi,
        "sum_odjel": sum_odjel,
    }

    return render(request, "main/summary.html", context)


def upisivanje(request):
    form = ZaposleniciForm()
    odjeli = Odjeli.objects.all()
    if request.method == "POST":
        form = ZaposleniciForm(request.POST, request.FILES)
        date_str = request.POST.get("datepicker")
        if form.is_valid():
            zaposlenik = form.save(commit=False)
            if date_str:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                zaposlenik.trajanje = date

            zaposlenik.ime = zaposlenik.ime.capitalize()
            zaposlenik.prezime = zaposlenik.prezime.capitalize()

            zaposlenik.save()
            return redirect("summary")

    context = {"form": form, "odjeli": odjeli}
    return render(request, "main/upis_zaposlenika.html", context)


def zaposlenik(request, pk):
    zaposlenik = Zaposlenici.objects.get(id=pk)
    context = {"zaposlenik": zaposlenik}

    return render(request, "main/zaposlenik.html", context)


def obrisiZap(request, pk):
    zaposlenik = Zaposlenici.objects.get(id=pk)
    if request.method == "POST":
        zaposlenik.delete()
        return redirect("summary")

    return render(request, "main/brisanje_zap.html", {"obj": zaposlenik})


def odmorZap(request, pk):
    zaposlenik = Zaposlenici.objects.get(id=pk)
    context = {"zaposlenik": zaposlenik}
    if request.method == "POST":
        date1_str = request.POST.get("datepicker1")
        date2_str = request.POST.get("datepicker2")
        
        godisnji = request.POST.get("godisnji")
        slobodni = request.POST.get("slobodni")
        dopust = request.POST.get("dopust")

        if date1_str and date2_str:
            date1 = datetime.strptime(date1_str, "%Y-%m-%d").date()
            date2 = datetime.strptime(date2_str, "%Y-%m-%d").date()
            num_days = (date2 - date1).days

            if godisnji is not None and zaposlenik.br_dopust:
                zaposlenik.br_godisnji -= int(num_days)

            if slobodni is not None and zaposlenik.br_dopust:
                zaposlenik.br_slob -= int(num_days)

            if dopust is not None and zaposlenik.br_dopust:
                zaposlenik.br_dopust -= int(num_days)

        zaposlenik.save()
        url = reverse("zaposlenik", kwargs={"pk": pk})
        return redirect(url)
    return render(request, "main/zap_odmor.html", context)


def azuriranje(request, pk):
    zaposlenici = Zaposlenici.objects.get(id=pk)

    form = ZaposleniciForm(instance=zaposlenici, initial={"odjel": zaposlenici.odjel})
    date_str = request.POST.get("datepicker")

    if request.method == "POST":
        form = ZaposleniciForm(request.POST, request.FILES, instance=zaposlenici)
        if form.is_valid():
            form = form.save(commit=False)
            if date_str:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                form.trajanje = date
            form.ime = form.ime.capitalize()
            form.prezime = form.prezime.capitalize()
            form.save()
            url = reverse("zaposlenik", kwargs={"pk": pk})
            return redirect(url)
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "main/azuriraj_zap.html", context)
