const toggleBtn =document.querySelector('.btnShow');
const sidebar =document.querySelector('.BN');

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
    btnToggleDM = document.body;
    btnToggleDM.classList.toggle('Dark');
}