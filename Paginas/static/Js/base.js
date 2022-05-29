const toggleBtn =document.querySelector('.btnShow');
const sidebar =document.querySelector('.BN');
var openMenu = document.querySelector(".img-header");
const menu = document.querySelector(".menu")
const teste = document.querySelector(".teste")
const textoMudarTema = document.querySelector('.changeTheme')
const btnToggleDM = document.body;


toggleBtn.addEventListener('click', function()
{
    sidebar.classList.toggle('BNtoggle');
});

closeBtn.addEventListener('click', function()
{
    sidebar.classList.remove('BNtoggle');
});

function toggleDarkMode()
{
    btnToggleDM.classList.toggle('Dark');
}

function openMenuFunction()
{
    menu.classList.toggle("menu-show");
}



