from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    default_room_members_count = 1
    appliance_type = (TV, )

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_room_members_count)
        self.calculate_expenses(self.appliances)
