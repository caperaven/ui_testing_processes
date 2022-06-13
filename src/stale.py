from selenium.common.exceptions import InvalidSelectorException, StaleElementReferenceException


def is_stale(element):
    try:
        element.is_enabled()
        return False
    except InvalidSelectorException as e:
        raise e
    except StaleElementReferenceException:
        return True