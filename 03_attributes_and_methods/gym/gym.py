class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        current_customer = [c for c in self.customers if current_subscription.customer_id == c.id][0]
        current_trainer = [t for t in self.trainers if t.id == current_subscription.trainer_id][0]
        current_plan = [p for p in self.plans if p.id == current_trainer.id][0]
        current_equipment = [e for e in self.equipment if e.id == current_plan.equipment_id][0]

        return f"{current_subscription}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}"



