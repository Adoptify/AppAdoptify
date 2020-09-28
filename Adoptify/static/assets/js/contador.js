const descripcion = document.querySelector('#descripcion');
const max = 300;
let display = document.querySelector('#display');
descripcion.addEventListener('input', () => {
	display.textContent = `${descripcion.value.length}/${max}`;
});
