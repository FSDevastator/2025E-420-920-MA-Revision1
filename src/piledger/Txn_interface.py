
from abc import ABC, abstractmethod

class LedgerTxn(ABC):
    #Simple Ledger transaction interface model
    def __init__(self,txn_no:int,date:str,account:str,amount:float):
        self._txn_no=int(txn_no)
        self._date=date
        self._account=account
        self._amount=amount

    @property
    def txn_no(self):
        return self._txn_no
    @txn_no.setter
    def txn_no(self,txn_no):
        self._txn_no=txn_no
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        self._date=date
    
    @property
    def account(self):
        return self._account
    @account.setter
    def account(self,account):
        self._account=account
    
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,amount):
        self._amount=amount
