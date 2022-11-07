
class Init:
    def __init__(self):
        self.dict = {}

    def set_value(self, key, val):
        self[key] = val

    def get_value(self, key):
        if key in self:
            return self[key]
        return None

    def delete_value(self, key):
        if key in self:
            c = self[key]
            del self[key]
            return c
        return None
