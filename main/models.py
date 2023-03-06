from django.db import models

# Opcije odabira
SPOL_ZAP = (("M", "Muško"), ("Z", "Žensko"), ("O", "Ostalo"), ("NE", "Ne želim reći"))
VRSTA_ODABIR = (("odredeno", "Određeno"), ("neodredeno", "Neodređeno"))


class Odjeli(models.Model):
    odjeli_org = models.CharField(max_length=100)

    def __str__(self):
        return self.odjeli_org


class Zaposlenici(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    slika = models.ImageField(null=True, default="avatar.svg")
    spol = models.CharField(max_length=2, choices=SPOL_ZAP)
    god_rod = models.PositiveIntegerField()
    pocetak_rada = models.DateField(auto_now_add=True)
    vrsta_ugovora = models.CharField(max_length=10, choices=VRSTA_ODABIR)
    trajanje = models.DateField(blank=True, null=True)
    odjel = models.ForeignKey("Odjeli", on_delete=models.SET_NULL, null=True)

    # Godisnji
    br_godisnji = models.PositiveIntegerField(blank=True, null=True)
    br_slob = models.PositiveIntegerField(blank=True, null=True)
    br_dopust = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.ime} {self.prezime}"
