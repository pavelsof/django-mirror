const djangoMirror = (function() {
	'use strict';

	const initMirror = function(element) {
		let mirror = CodeMirror.fromTextArea(element, {
			'mode': 'markdown'
		});
	};

	let mirrors = Object.create(null);

	document.addEventListener('DOMContentLoaded', () => {
		document.querySelectorAll('textarea.django-mirror-area').forEach(initMirror);
	})
}());
