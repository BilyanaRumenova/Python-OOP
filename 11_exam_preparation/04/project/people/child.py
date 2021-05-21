class Child:
    days_in_month = 30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = sum(toys_cost) + food_cost

    def get_monthly_expense(self):
        cost_for_month = self.cost * self.days_in_month
        return cost_for_month
        