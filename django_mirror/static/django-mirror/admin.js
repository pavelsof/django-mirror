document.addEventListener('DOMContentLoaded', function() {
	'use strict';

	document.querySelectorAll('.inline-group').forEach(function(container) {
		container.querySelectorAll('.empty-form textarea[data-mirror]').forEach(djangoMirror.removeMirror);

		const observer = new MutationObserver(function(records) {
			records.forEach((record) => {
				record.addedNodes.forEach((node) => {
					if (node.nodeType == 1) {
						node.querySelectorAll('textarea[data-mirror]').forEach(djangoMirror.initMirror);
					}
				});
			});
		});

		observer.observe(container, {childList: true, subtree: true});
	});
});
