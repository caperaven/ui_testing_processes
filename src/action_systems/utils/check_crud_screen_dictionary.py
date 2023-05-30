from src.data import state

def get_intent (name):
    defaults = state["crud-dictionary"]["default"]
    actions = state["crud-dictionary"].get(name, [])
    return defaults + actions # create a new array with defaults and actions in it.