from src.elements import get_element
from selenium.webdriver.common.by import By
from src.utils import has_shadow_root

ignore_tag_names = ["style", "text", "svg", "label", "slot"]

class TestScraper:
    def __init__(self):
        self.args = None
        self.path = None
        self.results = None

    async def run(self, driver, args, results):
        self.args = args
        start = args["query"]
        self.path = [start]
        self.results = []
        element = get_element(driver, args, results)
        self.validate_element(element)

        if len(self.results) == 0:
            results[args["step"]] = "success"
        else:
            results[args["step"]] = self.results

        self.args = None
        self.path = None
        self.results = None

    def validate_element(self, element):
        if ignore_tag_names.__contains__(element.tag_name):
            return

        if should_have_id(element):
            element_id = str(element.get_attribute("id"))
            data_id = str(element.get_attribute("data-id"))

            if (len(element_id) == 0 or element_id == "None") and (len(data_id) == 0 or data_id == "None"):
                self.results.append(' '.join(self.path))

        if element.tag_name.__contains__("button"):
            return

        self.validate_children(element)

    def validate_children(self, element):
        if has_shadow_root(element) is True:
            message = "shadow_root"
            identity = self.get_identity(element)
            if identity is not None:
                message = "#{} - shadow_root".format(identity)

            self.path.append(message)
            children = element.shadow_root.find_elements(By.CSS_SELECTOR, ":scope > *")
            self.process_children(children)
            del self.path[-1]

        children = element.find_elements(By.CSS_SELECTOR, ":scope > *")
        self.process_children(children)

    def process_children(self, children):
        if children is None or len(children) == 0:
            return

        index = 0
        for child in children:
            identity = self.get_identity(child)
            if identity is not None:
                self.path.append("{} - nth({} - #{})".format(child.tag_name, index, identity))
            else:
                self.path.append("{} - nth({})".format(child.tag_name, index))
            self.validate_element(child)
            del self.path[-1]
            index += 1
        pass

    def get_identity(self, element):
        element_id = element.get_attribute("data-id")
        if element_id is not None:
            return "#{}".format(element_id)

        role = element.get_attribute("role")
        if role is not None:
            return '[role="{}"]'.format(role)

        classes = element.get_attribute("class")
        if classes:
            return '[classes="{}"]'.format(classes)

        return None


required_tag_names = ["input", "button", "select", "ul", "textarea"]

roles = [
    "menuitem",
    "scrollbar",
    "searchbox",
    "separator",
    "slider",
    "spinbutton",
    "switch",
    "tab",
    "tabpanel",
    "treeitem",
    "combobox",
    "menu",
    "menubar",
    "cell",
    "columnheader",
    "row",
    "listitem",
    "button",
    "checkbox",
    "gridcell",
    "link",
    "menuitem",
    "menuitemcheckbox",
    "menuitemradio",
    "option",
    "radio",
    "textbox"]


def should_have_id(element):
    if required_tag_names.__contains__(element.tag_name):
        return True

    if element.tag_name.__contains__("button"):
        return True

    tab_index = element.get_attribute("tabindex")
    if tab_index == 0 or tab_index == -1:
        return True

    role = element.get_attribute("role")
    if roles.__contains__(role):
        return True

    return False

