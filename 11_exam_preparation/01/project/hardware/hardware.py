class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption <= self.available_capacity and software.memory_consumption <= self.available_memory:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - self.used_memory
    
    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity
    
    @property
    def used_memory(self):
        return sum([software.memory_consumption for software in self.software_components])

    @property
    def used_capacity(self):
        return sum([software.capacity_consumption for software in self.software_components])