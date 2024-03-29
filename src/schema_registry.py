import json
import os
import sys
from src.data import state


class SchemaRegistry:
    def __init__(self):
        self.current_index = 0
        self.login = None
        self.templates = {}
        self.schemas = []

        if "--settings" in sys.argv:
            settingsPath = sys.argv[sys.argv.index("--settings") + 1]
            self.load_settings(settingsPath)

        if "--login" in sys.argv:
            index = sys.argv.index("--login")
            self.schemas.append(get_file_path(sys.argv[index + 1]))

        if "--file" in sys.argv:
            index = sys.argv.index("--file")
            self.schemas.append(get_file_path(sys.argv[index + 1]))

        if "--folder" in sys.argv:
            index = sys.argv.index("--folder")
            self.load_folder(sys.argv[index + 1])

        if "--templates" in sys.argv:
            index = sys.argv.index("--templates")
            self.load_templates(sys.argv[index + 1])

        if "--server" in sys.argv:
            index = sys.argv.index("--server")
            state["server"] = sys.argv[index + 1]

    def load_settings(self, settingsPath):
        file = open(settingsPath)
        data = json.load(file)
        file.close()

        if "login" in data:
            self.schemas.append(get_file_path(data["login"]))

        if "file" in data:
            self.schemas.append(get_file_path(data["file"]))

        if "folder" in data:
            self.load_folder(get_file_path(data["folder"]))

        if "templates" in data:
            self.load_templates(get_file_path(data["templates"]))

        if "server" in data:
            state["server"] = data["server"]

        if "crud-dictionary" in data:
            state["crud-dictionary"] = data["crud-dictionary"]
        pass

    def add(self, schema):
        schema_id = schema["id"]
        self.schemas[schema_id] = schema
        pass

    def remove(self, schema_id):
        del self[schema_id]
        pass

    def load_folder(self, folder):
        for root, dirnames, filenames in os.walk(folder):
            if root.__contains__("template"):
                continue
            folder = os.path.realpath(root)
            for filename in filenames:
                if not filename.endswith(".json"):
                    continue
                file = os.path.join(folder, filename)
                if not file.__contains__("skip.") and file != self.login:
                    self.schemas.append(file)

    def load_templates(self, folder):
        for root, dirnames, filenames in os.walk(folder):
            folder = os.path.realpath(root)
            for filename in filenames:
                file = os.path.join(folder, filename)
                if not file.__contains__("skip.") and file != self.login:
                    content = from_file(file)
                    content_id = content["id"]
                    self.templates[content_id] = content

    def get_next_schema(self):
        if self.current_index >= len(self.schemas):
            return None

        schema = from_file(self.schemas[self.current_index])
        schema["name"] = os.path.basename(self.schemas[self.current_index])
        self.current_index += 1
        return schema.copy()

    def get_template(self, schema):
        return self.templates[schema]


def get_file_path(file):
    if os.path.isabs(file):
        return os.path.realpath(file)
    else:
        result = os.path.join(os.getcwd(), file)
        return os.path.realpath(result)


def from_file(file_path):
    file = open(file_path)
    data = json.load(file)
    file.close()
    data["file_path"] = file_path
    return data