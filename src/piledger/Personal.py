import os
import csv
from pathlib import Path
from datetime import datetime


class PersonalTxn():
    def __init__(self):
        self.__transactions=[dict]

    def load_data(self, filename):

        base_path=os.getcwd()
        search_path=Path(base_path)
        search_path=search_path.joinpath(filename)
        
        found_file=False

        try:
            found_file=False

            while(found_file==False):
                
                if (search_path.exists()):

                    with open(search_path,'r', encoding='utf-8') as file:
                        reader=csv.DictReader(file)
                        self.__transactions=list(reader)
                    found_file=True
                else:
                    if(search_path.joinpath('pyproject.toml').exists()):
                        raise FileNotFoundError(filename)     
                    else:
                        search_path = search_path.parent.parent
                        search_path=search_path.joinpath(filename)
        except FileNotFoundError as e:
            print(f"Erreur: fichier {e} introuvable.")

                
    def calculate_balance(self, acctname):
        
        bal = 0.0
        for eachtxn in self.__transactions:
            if eachtxn.get('Compte')==acctname:
                bal += float(eachtxn.get("Montant"))
        return bal

    def get_all_accounts(self):
        accts=[]
        for eachtxn in self.__transactions:
            accts.append(eachtxn['Compte'])
        return set(accts)
    
    def display_all_transactions(self):
        print("\n=== TOUTES LES TRANSACTIONS ===")
        for eachtxn in self.__transactions:
            print(f"Transaction: {eachtxn['No txn']} - date: {eachtxn['Date']}")
            print(f"Compte: {eachtxn['Compte']} - montant: {float(eachtxn['Montant']):.2f}$")
            if eachtxn['Commentaire']:
                print(f"Commentaire: {eachtxn['Commentaire']}")
            print()

    def display_transactions_byaccount(self, acctname):

        print(f"Transactions pour le compte '{acctname}':\n")
        count=0
        for eachtxn in self.__transactions:
            if eachtxn['Compte']==acctname:
                count+=1
                print(f"Transaction: {eachtxn['No txn']} - date: {eachtxn['Date']}")
                print(f"montant: {float(eachtxn['Montant']):.2f}$")
                if eachtxn['Commentaire']:
                    print(f"Commentaire: {eachtxn['Commentaire']}")
                print()
        if count==0:
            print(f"Aucune transaction trouvée pour le compte {acctname}.\n")
        else:
            print(f"{count} transactions trouvées pour le compte {acctname}\n")

    def display_summary(self):
        print("\n=== RÉSUMÉ DES COMPTES ===")
        accounts= self.get_all_accounts()

        for acct in accounts:
            balance=self.calculate_balance(acct)
            print(f"{acct}: {balance:.2f}$")

    def get_transactions_by_date_range(self, start_date, end_date):
        valid_txns=[]
        date_format="%Y-%m-%d"

        print(datetime.strptime(start_date, date_format).date())
        for eachtxn in self.__transactions:
            if (datetime.strptime(eachtxn['Date'],
                            date_format)).date() >= (datetime.strptime(start_date,date_format)).date():
                if (datetime.strptime(eachtxn['Date'],
                            date_format)).date() <= (datetime.strptime(end_date,date_format)).date():
                
                    valid_txns.append(eachtxn)
        
        if (valid_txns):
            return valid_txns 
        else: 
            print(f"Aucune transaction entre {start_date} et {end_date}.")
            return valid_txns        

    def find_largest_expense(self):
        filtered_expenses= [eachtxn for eachtxn in self.__transactions if eachtxn['Compte']!='Revenu' and eachtxn['Compte']!='Compte courant']
        max_expense = max(float(item['Montant']) for item in filtered_expenses)
        return max_expense

    def find_total_income(self):
        total=0
        for eachtxn in self.__transactions:
            if eachtxn['Compte']=='Revenu':
                total += abs(float(eachtxn['Montant']))
        return total

    def find_total_expenses(self):
        filtered_expenses= [eachtxn for eachtxn in self.__transactions if eachtxn['Compte']!='Revenu' and eachtxn['Compte']!='Compte courant']
        return sum([float(eachtxn['Montant']) for eachtxn in filtered_expenses])
    
    
    
