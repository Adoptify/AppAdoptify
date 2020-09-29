let displayMensaje = document.querySelector('#mensaje');
const mensajes = [ 'uno', 'dos', 'tres' ];

window.addEventListener('load', () => {
	random = Math.floor(Math.random() * mensajes.length);
	displayMensaje.textContent = mensajes[random];
});
