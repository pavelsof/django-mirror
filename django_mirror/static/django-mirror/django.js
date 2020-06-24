const djangoMirror = (function() {
	'use strict';

	const initMirror = function(element) {
		let options = JSON.parse(element.dataset.mirror);
		let mirror = CodeMirror.fromTextArea(element, options);
	};

	let mirrors = Object.create(null);

	document.addEventListener('DOMContentLoaded', () => {
		document.querySelectorAll('textarea[data-mirror]').forEach(initMirror);
	})
}());
