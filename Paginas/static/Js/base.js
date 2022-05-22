const toggleBtn =document.querySelector('.btnOpen');
const sidebar =document.querySelector('.BN');

toggleBtn.addEventListener('click', function()
{
    sidebar.classList.toggle('BNtoggle');
});

closeBtn.addEventListener('click', function()
{
    sidebar.classList.remove('BNtoggle');
});

function changeurl()
{
    var logo = document.querySelector('.mini-logo')
    url = "../../static/imagens/threeBars.png"
    logo.src = url
}

function returnurl()
{
    var logo = document.querySelector('.mini-logo')
    url = "../../static/imagens/mini-logo.jpeg"
    logo.src = url
}