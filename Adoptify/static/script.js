const descripcion = document.getElementById('descripcion');
descripcion.addEventListener('input', (evt) => {
	const display = document.getElementById('display');
	display.textContent = `${evt.target.value.length}/300`;
});
