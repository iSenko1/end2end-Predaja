flatpickr("#datepicker1, #datepicker2", {
    dateFormat: "Y-m-d",
    //minDate: "today"
});

var vrstaUgovoraField = document.getElementById("id_vrsta_ugovora");
var trajanjeOptField = document.getElementById("trajanje-opt");

function showHideTrajanjeOptField() {
    if (vrstaUgovoraField.value === "odredeno") {
        flatpickr("#datepicker", {
            dateFormat: "Y-m-d",
            minDate: "today"
        });
        trajanjeOptField.style.display = "block";
    } else {
        trajanjeOptField.style.display = "none";
    }
}

// poziv funkcije kod otvaranja prozora
showHideTrajanjeOptField();

// poziv funkcije kad se vrsta ugovora promjeni i ako je odredeno, prikaze se polje
vrstaUgovoraField.addEventListener("change", showHideTrajanjeOptField);


// prikaz nove azurirane slike i micanje sakrij klase kod upisa zaposlenika
function previewImage(event) {
    var input = event.target;
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        var previewImg = document.getElementById("preview-img");
        previewImg.classList.remove("sakrij");
        previewImg.src = e.target.result;
      };
      reader.readAsDataURL(input.files[0]);
    }
  }
  

  function toggleNavbar() {
    var navbar = document.querySelector(".navbar");
    navbar.classList.toggle("responsive");
  }
  