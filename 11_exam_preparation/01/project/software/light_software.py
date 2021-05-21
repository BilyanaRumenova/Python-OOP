from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", int(1.5 * capacity_consumption), int(0.5 * memory_consumption))
