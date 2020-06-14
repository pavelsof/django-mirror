const djangoMirror = (function() {
	'use strict';

	const initMirror = function(element) {
		let data = element.dataset.mirror;
		let mirror = CodeMirror.fromTextArea(element, {
			'mode': data
		});
	};

	let mirrors = Object.create(null);

	document.addEventListener('DOMContentLoaded', () => {
		document.querySelectorAll('textarea[data-mirror]').forEach(initMirror);
	})
}());
