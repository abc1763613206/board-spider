import json
import typing


class Image:
    def __init__(self, url: str = None, base64: str = None):
        self.url = url
        self.base64 = base64

    @property
    def get_dict(self):
        obj = {}

        if self.url is not None:
            obj['url'] = self.url

        if self.base64 is not None:
            obj['base64'] = self.base64

        return obj

    def from_dict(self, d: typing.Any):
        if "url" in d.keys():
            self.url = d["url"]

        if "base64" in d.keys():
            self.base64 = d["base64"]

    @property
    def get_json(self):
        return json.dumps(self.get_dict)

    def from_json(self, json_string: str):
        self.from_dict(json.loads(json_string))


class Color:
    def __init__(self, color: str, background_color: str):
        self.color = color
        self.background_color = background_color

    @property
    def get_dict(self):
        obj = {}

        obj["color"] = self.color
        obj["background_color"] = self.background_color

        return obj

    def from_dict(self, d: typing.Any):
        if "color" in d.keys():
            self.color = d["color"]

        if "background_color" in d.keys():
            self.background_color = d["background_color"]

    @property
    def get_json(self):
        return json.dumps(self.get_dict)

    def from_json(self, json_string: str):
        self.from_dict(json.loads(json_string))
