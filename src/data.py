data = {
    "scripts": {
        "is_ready": "document.querySelector('{}').addEventListener('isReady', (e) => e.target.dataset.ready = true)",
        "idle-false": "document.body.setAttribute('idle', false)",
        "idle-true": "if (globalThis.crsbinding != null) {globalThis.crsbinding.idleTaskManager.add(() => document.body.setAttribute('idle', true))} else {document.body.setAttribute('idle', true)}",
        "shadow-query": "document.querySelector('{}').shadowRoot.querySelector('{}');"
    }
}

state = {
}