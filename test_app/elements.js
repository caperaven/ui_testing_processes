export default class ElementsViewModel extends crsbinding.classes.ViewBase {
    async connectedCallback() {
        await super.connectedCallback();
        this.setProperty("myValue", Date.now());
    }
}