class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
b2 = Bank()
Bank.change_bank_name("New Bank")
print(b1.bank_name)
print(b2.bank_name)