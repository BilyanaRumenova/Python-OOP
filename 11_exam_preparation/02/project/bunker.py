class Bunker():
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if len(foods) == 0:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        water = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if len(water) == 0:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if len(painkillers) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        if len(salves) == 0:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        else:
            self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                med = self.painkillers[-1]
                med.apply(survivor)
            elif medicine_type == "Salve":
                med = self.salves[-1]
                med.apply(survivor)
            del self.medicine[-1]
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                f = self.food[-1]
                f.apply(survivor)
            elif sustenance_type == "WaterSupply":
                w = self.water[-1]
                w.apply(survivor)
            del self.supplies[-1]
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")

# from project.supply.supply import Supply
# from project.survivor import Survivor
#
#
# class Bunker:
#     def __init__(self):
#         self.survivors = []
#         self.supplies = []
#         self.medicine = []
#
#     @property
#     def food(self):
#         food = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
#         if len(food) == 0:
#             raise IndexError("There are no food supplies left!")
#         return food
#
#     @property
#     def water(self):
#         water = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
#         if len(water) == 0:
#             raise IndexError("There are no water supplies left!")
#         return water
#
#     @property
#     def painkillers(self):
#         painkillers = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
#         if len(painkillers) == 0:
#             raise IndexError("There are no painkillers left!")
#         return painkillers
#
#     @property
#     def salves(self):
#         salves = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
#         if len(salves) == 0:
#             raise IndexError("There are no salves left!")
#         return salves
#
#     def add_survivor(self, survivor):
#         if survivor not in self.survivors:
#             self.survivors.append(survivor)
#
#     def add_supply(self, supply):
#         self.supplies.append(supply)
#
#     def add_medicine(self, medicine):
#         self.medicine.append(medicine)
#
#     def heal(self, survivor, medicine_type):
#         if survivor.needs_healing:
#             if medicine_type == "Painkiller":
#                 last_med = self.painkillers[-1]
#                 last_med.apply(survivor)
#                 self.painkillers.pop()
#
#             elif medicine_type == "Salve":
#                 last_med = self.salves[-1]
#                 last_med.apply(survivor)
#                 self.salves.pop()
#
#             return f"{survivor.name} healed successfully with {medicine_type}"
#
#     def sustain(self, survivor, sustenance_type):
#         if survivor.needs_sustenance:
#             if sustenance_type == "FoodSupply":
#                 last_f = self.food[-1]
#                 last_f.apply(survivor)
#                 self.food.pop()
#             elif sustenance_type == "WaterSupply":
#                 last_w = self.water[-1]
#                 last_w.apply(survivor)
#                 self.water.pop()
#
#             return f"{survivor.name} sustained successfully with {sustenance_type}"
#
#     def next_day(self):
#         for survivor in self.survivors:
#             survivor.needs -= survivor.age * 2
#             self.sustain(survivor, "FoodSupply")
#             self.sustain(survivor, "WaterSupply")
#
#
#
#
#
#
