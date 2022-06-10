def evaluate(expr, context, process=None, item=None):
    return eval(clean_exp(expr), {
        "context": context,
        "process": process,
        "item": item
    })


def clean_exp(expr):
    if not expr.__contains__("."):
        return expr

    expr = expr.replace(" || ", " or ").replace(" && ", " and ")

    parts = expr.split(" ")
    for i in range(0, len(parts)):
        path = parts[i]
        if path.__contains__("."):
            path_parts = path.split(".")
            result_parts = [path_parts[0]]

            for j in range(1, len(path_parts)):
                result_parts.append('["{}"]'.format(path_parts[j]))

            new_expr = "".join(result_parts)
            parts[i] = new_expr

    return " ".join(parts)