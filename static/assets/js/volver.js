const goBack = () => {
	if (document.referrer == document.location.href) {
		window.history.go(-2);
	} else {
		window.history.back();
	}
};
