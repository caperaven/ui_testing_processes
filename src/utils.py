def get_name(args):
    if "id" in args:
        return args["id"]

    if "query" in args:
        return args["query"]


def get_eval(args):
    if "eval" in args:
        return args["eval"]
    else:
        return None


def has_shadow_root(element):
    result = True
    try:
        root = element.shadow_root
        if root is None:
            result = False
    except Exception as e:
        result = False

    return result
