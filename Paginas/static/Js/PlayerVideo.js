function loadVideo()
{
    btn = document.querySelectorAll('.btn')
    btnPlay = document.querySelector('.playBtn')
    var urlVideo = btn[0].getAttribute('id');
    video.src = urlVideo;
    video.play()
    btnPlay.style.display = "none";
    console.log(urlVideo);
}

let video = document.querySelector('video');
video.ontimeupdate = function() {videoTracking()};
let cb = document.querySelector('.cb');

document.querySelectorAll('.btn').forEach(btn =>
{
    btn.addEventListener('click', event =>
    {
        btnPlay = document.querySelector('.playBtn')
        btnPlay.style.display = "none";
        let url = btn.getAttribute('id');
        video.src = url;
    })
})

function videoTracking()
{
    videoPercentage = (video.duration * 90) / 100;
    if(video.currentTime >= videoPercentage)
    {
        cb.checked = true;
    }
}