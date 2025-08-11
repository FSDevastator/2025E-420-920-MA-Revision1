from Txn_interface import LedgerTxn

class GeneralTxn(LedgerTxn):
    def init(self,txn_no,date,account,amount,comment):
        self._txn_no=txn_no
        self._date=date
        self._account=account
        self._amount=float(amount)
        self._comment=comment
    
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

    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self,comment):
        self._comment=comment
