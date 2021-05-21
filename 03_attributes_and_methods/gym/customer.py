class Customer:
    customer_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1



from attributes_and_methods_EXERCISES.gym.project.equipment import Equipment
from attributes_and_methods_EXERCISES.gym.project.exercise_plan import ExercisePlan
from attributes_and_methods_EXERCISES.gym.project.gym import Gym
from attributes_and_methods_EXERCISES.gym.project.subscription import Subscription
from attributes_and_methods_EXERCISES.gym.project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
