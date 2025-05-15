class Bank:
    bank_name = "First National"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Test
b1 = Bank()
b2 = Bank()
Bank.change_bank_name("City Bank")
print(b1.bank_name)
print(b2.bank_name)