# Deadlock Prevention
import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
    
    def transfer(self, amount, other_account):
        # Acquire locks in sorted order to prevent deadlock
        account1, account2 = sorted([self, other_account], key=id)
        with account1.lock:
            with account2.lock:
                if self.balance >= amount:
                    self.balance -= amount
                    other_account.balance += amount
                    print(f'Transfer {amount} successful')

acc1 = BankAccount(100)
acc2 = BankAccount(50)
acc1.transfer(20, acc2)
