from src.elements import get_element
from src.utils import get_eval


def _element_condition(args, results):
    def _predicate(driver):
        try:
            element = get_element(driver, args, results)

            if element is None:
                return False

            size = element.size
            if size["width"] == 0 or size["height"] == 0:
                return False
            else:
                return True
        except Exception as e:
            return False

    return _predicate


def _is_ready_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute("data-ready")
        if value is None:
            return False
        else:
            return True

    return _predicate


def _is_enabled_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute("disabled")
        return value is None

    return _predicate


def _text_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.text
        exp_value = args["value"]
        return _eval(value, exp_value, args)

    return _predicate


def _attribute_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute(args["attr"])
        exp_value = args["value"]
        return _eval(value, exp_value, args)

    return _predicate


def _css_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        prop = args['property']
        value = element.value_of_css_property(prop)
        exp_value = args["value"]
        return _eval(value, exp_value, args)

    return _predicate


def _property_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        prop = args["property"]
        value = element.get_property(prop)
        exp_value = args["value"]
        return _eval(value, exp_value, args)

    return _predicate


def _class_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        cls = element.get_attribute("class")
        sub = args["class"]
        return sub in cls

    return _predicate


def _count_condition(args, results):
    def _predicate(driver):
        query = args["query"]
        count = args["count"]
        all_children_by_css = driver.find_elements_by_css_selector(query)

        count_value = len(all_children_by_css)
        return _eval(count_value, count, args)
    return _predicate


def _selected_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = args["value"] or False
        return element.is_selected() == value

    return _predicate


def _window_count_condition(args, results):
    def _predicate(driver):
        count = int(args["count"])
        length = len(driver.window_handles)
        return length == count

    return _predicate


def _eval(value1, value2, args):
    evaluator = get_eval(args)

    match evaluator:
        case "lt":
            return value1 < value2
        case "gt":
            return value1 > value2
        case "ne":
            return value1 != value2
        case default:
            return value1 == value2


def _idle_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, {"query": "body"}, results)
        value = element.get_attribute("idle")
        return value == "true"
    return _predicate

