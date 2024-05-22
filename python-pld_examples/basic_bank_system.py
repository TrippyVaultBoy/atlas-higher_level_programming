#!/usr/bin/python


class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(amount):
        balance += amount
    def withdraw(amount):
        balance -= amount


class SavingsAccount(Account):
    def __init__(self, account_number, balance, intrest_rate):
        super().__init__(account_number, balance)
        self.__intrest_rate = intrest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.__overdraft_limit = overdraft_limit
