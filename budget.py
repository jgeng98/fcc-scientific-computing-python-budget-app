class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        return

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction.get("amount")
        return balance

    def transfer(self, amount, category):
        pass

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    pass


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(900, "deposit")
    food.withdraw(100, "eggs")
    print(food.get_balance())
    print(food.ledger)
