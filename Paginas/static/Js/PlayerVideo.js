window.send = 1;
let video = document.querySelector('video');
video.ontimeupdate = function() {videoTracking()};
desc = document.querySelector('.descricao-video');
window.id_aula = 0;

function loadVideo()
{
    btn = document.querySelectorAll('.videoBtn');
    btnPlay = document.querySelector('.playBtn');
    var urlVideo = btn[0].getAttribute('data-url');
    video.src = urlVideo;
    btnPlay.style.display = "none";
    console.log(urlVideo);
    window.id_aula = btn[0].getAttribute('id')
    btns()
}

function btns()
{
    let atual = document.querySelector('.videos')
    limparSelecionados(atual)
    addClassList(atual)
}

document.querySelectorAll('.videoBtn').forEach(btn =>
{
    btn.addEventListener('click', event =>
    {
        btnPlay = document.querySelector('.playBtn')
        btnPlay.style.display = "none";
        let url = btn.getAttribute('data-url');
        window.id_aula = btn.getAttribute('id')
        video.src = url;

        let atual = btn.querySelector('.videos')
        limparSelecionados(atual)
        addClassList(atual)
    })
})

function addClassList(atual)
{
    atual.classList.add('aulaSelecionada')
}

function limparSelecionados(atual)
{
    window.send = 1
    let elements = document.querySelectorAll(".videos")
    for (var i = 0; i < elements.length; i++) {
        let element = elements[i]
        if (element != atual && element.classList.contains('aulaSelecionada')) {
            element.classList.remove('aulaSelecionada')
        }
    }
}

function videoTracking()
{
    videoPercentage = (video.duration * 90) / 100;
    if (video.currentTime >= videoPercentage) {
        document.querySelector('.aulaSelecionada')
            .querySelector('.finalizado')
            .classList
            .add('aulaFinalizada')

        if (window.send === 1) {
            enviarAulaFinalizada(window.id_aula);
            window.send = 0;
        }
    }
}

function enviarAulaFinalizada(id)
{
    let data = {
        aula: id,
        curso: document.getElementById('curso').value,
    }

    fetch("/aula/assistida", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
}

document.addEventListener(onload, loadVideo())