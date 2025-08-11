
from abc import ABC, abstractmethod

class LedgerTxn(ABC):
    #Simple Ledger transaction interface model

    @property
    @abstractmethod
    def txn_no(self):
        pass

    @property
    @abstractmethod
    def date(self):
        pass

    @property
    @abstractmethod
    def account(self):
        pass

    @property
    @abstractmethod
    def amount(self):
        pass
