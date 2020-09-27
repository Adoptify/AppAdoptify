const descripcion = document.querySelector('#descripcion');
const max = 300;
let bar = document.querySelector('.progress-bar');
bar.style.width = '0%';
let progreso = 0;
descripcion.addEventListener('input', () => {
	bar.style.width = `${descripcion.value.length * 100 / max}%`;
});
