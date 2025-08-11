from Txn_interface import LedgerTxn

class PurchaseTxn(LedgerTxn):
    def init(self,txn_no,date,invoiceno,supplier,materials,comment):
        self._txn_no=txn_no
        self._date=date
        self._invoiceno=invoiceno
        self._supplier=supplier
        self._materials=materials
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
    def invoiceno(self):
        return self._invoiceno
    @invoiceno.setter
    def account(self,invoiceno):
        self._invoiceno=invoiceno
    
    @property
    def supplier(self):
        return self._supplier
    @supplier.setter
    def supplier(self,supplier):
        self._supplier=supplier

    @property
    def materials(self):
        return self._materials
    @materials.setter
    def materials(self,materials):
        self._materials=materials

    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self,comment):
        self._comment=comment