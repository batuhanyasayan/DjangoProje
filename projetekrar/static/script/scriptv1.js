// !NAVBAR-START
//* navbar kategori gizleme 
let navbarEye = document.getElementById('navbar-eye')
let navbarKategori = document.getElementById('navbar-kategori')
let navbarXmark = document.getElementById('navbar-xmark') 

if(navbarEye){
    navbarEye.addEventListener('click', toggleNavbar)
}
if(navbarXmark){
    navbarXmark.addEventListener('click',toggleNavbar)
}

function toggleNavbar(){
    navbarEye.classList.toggle('navbar-eye')
    navbarXmark.classList.toggle('navbar-xmark')
    navbarKategori.classList.toggle('navbar-kategori')
}

// !LİNK GRUBU DETAY BÖLÜMÜ
// Link grubu data ile yaptım
let aktifDiv = null;
function linkMenu(link){
    const linkGrupId = link.dataset.target;
    const linkGrup = document.getElementById(linkGrupId);
    if (aktifDiv !== null && aktifDiv !== linkGrup) {
        aktifDiv.style.display = "none";
    }
    linkGrup.style.display = linkGrup.style.display === "block" ? "none" : "block";
    aktifDiv = linkGrup.style.display === "block" ? linkGrup : null;
}

//!NAVBAR-HAMBURGER-MENU-START
function barMenu(){
    const barOpenElements = document.querySelectorAll('.bar-menu')
    barOpenElements.forEach((element) => {
        element.addEventListener('click',() =>{
            const hamburgerMenu = document.querySelector('.hamburger-menu')
            hamburgerMenu.classList.add('hamburger-menu-aktif')
            if(hamburgerMenu.classList.contains('hamburger-menu-aktif')){
            }
                
        })
    })

    const ok = document.querySelectorAll('.ok')
    ok.forEach((e) => {
        e.addEventListener('click', ()=>{
            const hamburgerMenu = document.querySelector('.hamburger-menu')
            if(hamburgerMenu.classList.contains('hamburger-menu-aktif')){
            hamburgerMenu.classList.remove('hamburger-menu-aktif')
            }
        })
    })
    
}
barMenu()


//!NAVBAR-HAMBURGER-MENU-END
//!NAVBAR-END

// ALED-BURCU SON JS BAŞLANGIÇ
//! SCROLL BAR

const categoryScroller = document.getElementById("categoryScroller");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const scrollAmount = 300; // Kaydırma miktarı (px)

// Kategori carousel'ını başlangıçta odalar kategorisiyle başlatmak için aşağıdaki kodu ekleyin:
if(categoryScroller){
    categoryScroller.scrollLeft = 0;
}

if (prevBtn) {
  

prevBtn.addEventListener("click", () => {
  categoryScroller.scrollLeft -= scrollAmount;
  if (categoryScroller.scrollLeft < 0) {
    categoryScroller.scrollLeft = 0;
  }
});
}
if (nextBtn) {
  
nextBtn.addEventListener("click", () => {
  categoryScroller.scrollLeft += scrollAmount;
  if (
    categoryScroller.scrollLeft >
    categoryScroller.scrollWidth - categoryScroller.clientWidth
  ) {
    categoryScroller.scrollLeft =
      categoryScroller.scrollWidth - categoryScroller.clientWidth;
  }
});
}

const categoryScrollerr = document.getElementById("categoryScroller-2");
const prevBtnn = document.getElementById("prevBtn-2");
const nextBtnn = document.getElementById("nextBtn-2");
const scrollAmountt = 300; // Kaydırma miktarı (px)

// Kategori carousel'ını başlangıçta odalar kategorisiyle başlatmak için aşağıdaki kodu ekleyin:
if(categoryScroller){
    categoryScroller.scrollLeft = 0;
}

if(prevBtnn){

prevBtnn.addEventListener("click", () => {
  categoryScrollerr.scrollLeft -= scrollAmount;
  if (categoryScrollerr.scrollLeft < 0) {
    categoryScrollerr.scrollLeft = 0;
  }
});
}

if (nextBtnn) {
  
nextBtnn.addEventListener("click", () => {
  categoryScrollerr.scrollLeft += scrollAmount;
  if (
    categoryScrollerr.scrollLeft >
    categoryScrollerr.scrollWidth - categoryScrollerr.clientWidth
  ) {
    categoryScroller.scrollLeft =
      categoryScrollerr.scrollWidth - categoryScrollerr.clientWidth;
  }
});
}

//! Şifre değiştirme js

const newPasswordInput = document.getElementById("newPassword");
const confirmNewPasswordInput = document.getElementById("confirmNewPassword");
const requirements = document.querySelectorAll(".sifreOzellikleri p i");
const formInputs = document.querySelectorAll(".form-control");
const updateButton = document.getElementById("updateButton");
const passwordMismatchError = document.getElementById("passwordMismatchError");

if (newPasswordInput) {
  newPasswordInput.addEventListener("input", function () {
  const password = this.value;

  const hasMinimumLength = password.length >= 8;
  const hasLetter = /[a-zA-Z]/.test(password);
  const hasDigitOrSpecialChar = /[0-9!@#$%^&*()_+[\]{};':"\\|,.<>?]/.test(
    password
  );

  updateRequirement(requirements[0], hasMinimumLength);
  updateRequirement(requirements[1], hasLetter);
  updateRequirement(requirements[2], hasDigitOrSpecialChar);

  const isValid = hasMinimumLength && hasLetter && hasDigitOrSpecialChar;
  const formContainer = document.querySelector(".sifreDegistir");
  formContainer.classList.toggle("valid", isValid);
  });
}

if (confirmNewPasswordInput) {
  
confirmNewPasswordInput.addEventListener("input", function () {
  const newPassword = newPasswordInput.value;
  const confirmNewPassword = confirmNewPasswordInput.value;

  if (confirmNewPassword === newPassword) {
    confirmNewPasswordInput.classList.remove("error-input");
    passwordMismatchError.style.display = "none";
  } else {
    confirmNewPasswordInput.classList.add("error-input");
    passwordMismatchError.style.display = "block";
  }
});
}

function updateRequirement(requirementElement, isFulfilled) {
  const icon = requirementElement;
  icon.classList.toggle("fa-check-circle", isFulfilled);
  icon.classList.toggle("fa-circle-xmark", !isFulfilled);
  icon.style.color = isFulfilled ? "green" : "gray";
}

formInputs.forEach((input) => {
  input.addEventListener("input", function () {
    if (this.classList.contains("error-input")) {
      this.classList.remove("error-input");
    }
    if (this.value === "") {
      this.classList.add("error-input");
    }
  });
});

if(updateButton){

updateButton.addEventListener("click", function (event) {
  formInputs.forEach((input) => {
    if (input.value === "") {
      input.classList.add("error-input");
      event.preventDefault();
    }
  });

  if (newPasswordInput.value !== confirmNewPasswordInput.value) {
    confirmNewPasswordInput.classList.add("error-input");
    passwordMismatchError.style.display = "block";
    event.preventDefault();
  }
});
}

//! Bireysel ve Kurumsal Fatura
const buttons = document.querySelectorAll(".button-section");
const bireyselFatura = document.querySelector(".bireyselFatura");
const kurumsalFatura = document.querySelector(".kurumsalFatura");

// İlk yüklendiğinde Bireysel seçili olarak ayarla
// bireyselFatura.style.display = "flex";
// kurumsalFatura.style.display = "none";

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    buttons.forEach((btn) => btn.classList.remove("selected"));
    button.classList.add("selected");

    if (button.id === "bireysel") {
      bireyselFatura.style.display = "flex";
      kurumsalFatura.style.display = "none";
    } else if (button.id === "kurumsal") {
      bireyselFatura.style.display = "none";
      kurumsalFatura.style.display = "flex";
    }
  });
});

//! HOOVER ÖZELLİKLERİ

let biletEtkinliklinkss = document.querySelectorAll(".biletlerimEtkinlikHvr");

biletEtkinliklinkss.forEach((etkinlikLink) => {
  etkinlikLink.addEventListener("click", () => {
    const linkId = etkinlikLink.getAttribute("data-id");

    biletEtkinliklinkss.forEach((l) => {
      if (l.getAttribute("data-id") === linkId) {
        l.classList.toggle("active");
      } else {
        l.classList.remove("active");
      }
    });
  });
});


let basss = document.querySelector(".hesapAyarlariB");
if (basss) {
basss.addEventListener("click",
function hesapAyari(){


let hesapAyarlari = document.querySelector (".hessap")
hesapAyarlari.style.display = "block";

let hesapAyarlari2 = document.querySelector (".biletlerimBilgisag")
hesapAyarlari2.style.display = "none";


}
)};

let bass = document.querySelector(".biletlerimmm");
if (bass) {
bass.addEventListener("click",
function hesapAyarii(){


let hesapAyarlari4 = document.querySelector (".biletlerimBilgisag")
hesapAyarlari4.style.display = "block";

let hesapAyarlari3 = document.querySelector (".hessap")
hesapAyarlari3.style.display = "none";


}
)};


// ALED-BURCU SON JS SONUs