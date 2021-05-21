class Equipment:
    _id = 0

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment._id + 1