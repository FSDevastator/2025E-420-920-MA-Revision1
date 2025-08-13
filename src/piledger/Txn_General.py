from Txn_interface import LedgerTxn

class GeneralTxn(LedgerTxn):
    def __init__(self, txn_no: int, date: str, account: str, amount: float,comment:str):
        super().__init__(txn_no, date, account, amount)
        self.comment=comment
    
    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self,comment):
        self._comment=comment
