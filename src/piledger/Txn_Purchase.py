from Txn_interface import LedgerTxn

class PurchaseTxn(LedgerTxn):
    def __init__(self,txn_no:int,date:str, account:str,
                 amount:float,invoiceno:int,supplier:str,materials:str):
        super().__init__(txn_no,date,account,amount)
        self._invoiceno=invoiceno
        self._supplier=supplier
        self._materials=materials
          
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

    