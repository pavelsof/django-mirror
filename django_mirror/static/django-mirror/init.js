const djangoMirror = (function() {
	'use strict';

	// init a CodeMirror editor for the given <textarea>
	const initMirror = function(textarea) {
		let options = JSON.parse(textarea.dataset.mirror);
		CodeMirror.fromTextArea(textarea, options);
	};

	// remove the given <textarea>'s CodeMirror editor
	// assume that the editor was inited using CodeMirror.fromTextArea
	const removeMirror = function(textarea) {
		textarea.parentNode.querySelectorAll('.CodeMirror').forEach((div) => {
			if (div.hasOwnProperty('CodeMirror')) {
				let editor = div.CodeMirror;
				if (editor.getTextArea() == textarea) {
					editor.toTextArea();
				}
			}
		});
	};

	document.addEventListener('DOMContentLoaded', () => {
		document.querySelectorAll('textarea[data-mirror]').forEach(initMirror);
	});

	return {
		initMirror: initMirror,
		removeMirror: removeMirror,
	};
})();
