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