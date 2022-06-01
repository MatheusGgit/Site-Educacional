const toggleBtn =document.querySelector('.btnShow');
const sidebar =document.querySelector('.BN');
var openMenu = document.querySelector(".img-header");
const menu = document.querySelector(".menu")
const teste = document.querySelector(".teste")
const textoMudarTema = document.querySelector('.changeTheme')
const btnToggleDM = document.body;
const headerTxt = document.querySelector('.header-Text');
const menu_bars = document.querySelector('.fa-bars');


toggleBtn.addEventListener('click', function()
{
    sidebar.classList.toggle('BNtoggle');

    if (sidebar.className === 'BN BNtoggle')
    {
        menu_bars.style.marginLeft = "18.5rem";
    }
    else
    {
        menu_bars.style.marginLeft = "5.5rem";
    }
});

function openSideBar()
{
    sidebar.classList.toggle('BNtoggle');
}


function toggleDarkMode()
{
    btnToggleDM.classList.toggle('Dark');
}

function openMenuFunction()
{
    menu.classList.toggle("menu-show");
}




