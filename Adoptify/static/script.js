const descripcion = document.getElementsByName('textarea');
console.log(descripcion);
descripcion.addEventListener('input', (evt) => {
	console.log('holaa');
	const display = document.getElementById('display');
	display.textContent = `${evt.target.value.length}/300`;
});
