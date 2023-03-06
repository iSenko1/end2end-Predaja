from django.forms import ModelForm
from .models import Zaposlenici


class ZaposleniciForm(ModelForm):
    class Meta:
        model = Zaposlenici
        fields = "__all__"

        # exclude = ("trajanje",)

        labels = {
            "ime": "Ime",
            "prezime": "Prezime",
            "slika": "Slika",
            "spol": "Spol",
            "god_rod": "Godina rođenja",
            "vrsta_ugovora": "Vrsta ugovora",
            "trajanje": "Trajanje ugovora",
            "odjel": "Odjel",
            "br_godisnji": "Broj godišnjih odmora",
            "br_slob": "Broj slobodnih dana",
            "br_dopust": "Broj dana dopusta",
        }

    # def clean_title(self):
    #     return self.cleaned_data['ime'].capitalize()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ime"].widget.attrs.update({"class": "form-input"})
        self.fields["prezime"].widget.attrs.update({"class": "form-input"})
        self.fields["slika"].widget.attrs.update(
            {"class": "form-input fileUpload", "accept": "image/*"}
        )

        self.fields["spol"].widget.attrs.update({"class": "form-input"})
        self.fields["god_rod"].widget.attrs.update({"class": "form-input"})
        self.fields["vrsta_ugovora"].widget.attrs.update({"class": "form-input"})
        self.fields["trajanje"].widget.attrs.update({"class": "form-input"})
        self.fields["odjel"].widget.attrs.update({"class": "form-input"})
        self.fields["br_godisnji"].widget.attrs.update({"class": "form-input"})
        self.fields["br_slob"].widget.attrs.update({"class": "form-input"})
        self.fields["br_dopust"].widget.attrs.update({"class": "form-input"})
