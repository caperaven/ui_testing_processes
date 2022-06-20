import json
import os
import sys


class SchemaRegistry:
    def __init__(self):
        self.current_index = 0
        self.login = None
        self.templates = {}
        self.schemas = []

        if "--login" in sys.argv:
            index = sys.argv.index("--login")
            self.login = get_file_path(sys.argv[index + 1])

        if "--file" in sys.argv:
            index = sys.argv.index("--file")
            self.login = sys.argv[index + 1]
            self.files.append(get_file_path(self.login))

        if "--folder" in sys.argv:
            index = sys.argv.index("--folder")
            folder = sys.argv[index + 1]
            self.load_folder(folder)

        if "--templates" in sys.argv:
            index = sys.argv.index("--templates")
            folder = sys.argv[index + 1]
            self.load_templates(folder)

    def add(self, schema):
        schema_id = schema["id"]
        self.schemas[schema_id] = schema
        pass

    def remove(self, schema_id):
        del self[schema_id]
        pass

    def load_folder(self, folder):
        for root, dirnames, filenames in os.walk(folder):
            folder = os.path.realpath(root)
            for filename in filenames:
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
    return data