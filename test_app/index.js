export default class IndexViewModel extends crsbinding.classes.ViewBase {
    async connectedCallback() {
        await super.connectedCallback();
    }

    async login() {
        const dialog = document.querySelector("#dlgLogin");
        dialog.showModal();
    }

    async closeDialog() {
        const dialog = document.querySelector("#dlgLogin");
        dialog.close();
    }
}