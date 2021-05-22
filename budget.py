class Category:
    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.ledger = []

    def __transaction_formatter(self, transaction):
        trimmed_description = transaction.get("description")[:23].ljust(23)
        trimmed_amount = f"{transaction.get('amount'):.2f}"[:7].rjust(7)
        return trimmed_description + trimmed_amount

    def __str__(self):
        output = ""
        output += self.category.capitalize().center(30, "*") + "\n"
        for transaction in self.ledger:
            output += self.__transaction_formatter(transaction) + "\n"
        output += "Total: " + str(self.get_balance())
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        return

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_category.category)
            budget_category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    pass
