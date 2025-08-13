from Txn_interface import LedgerTxn


class GeneralTxn(LedgerTxn):
    def __init__(self, txn_no, date, account, amount,comment:str):
        super().__init__(txn_no, date, account, float(amount))
        self.comment=comment
    def __str__(self):
        if self.comment:
            return f"No txn: {self.txn_no} | Date: {self.date} | Compte: {self.account} | Montant: {self.amount:.2f}$ | Commentaire: {self.comment}\n"
        else:
            return f"No txn: {self.txn_no} | Date: {self.date} | Compte: {self.account} | Montant: {self.amount:.2f}$\n"
    
    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self,comment):
        self._comment=comment
