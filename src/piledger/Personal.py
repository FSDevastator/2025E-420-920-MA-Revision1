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
                    if not self.__transactions:
                        print(f"Fichier {filename} ne contient pas de transactions.  Aucunes données chargées.")
                    elif self.__transactions:
                        print(f"Données chargées avec succès.")                        
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
            print(f"{count} transaction(s) trouvée(s) pour le compte {acctname}\n")

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
        sorted_data = sorted(filtered_expenses, key=lambda x: float(x['Montant']), reverse=True)
        return sorted_data.pop(0)

    def find_total_income(self):
        total=0
        for eachtxn in self.__transactions:
            if eachtxn['Compte']=='Revenu':
                total += abs(float(eachtxn['Montant']))
        return total

    def find_total_expenses(self):
        filtered_expenses= [eachtxn for eachtxn in self.__transactions if eachtxn['Compte']!='Revenu' and eachtxn['Compte']!='Compte courant']
        return sum([float(eachtxn['Montant']) for eachtxn in filtered_expenses])
    
    def export_account_postings(self, accnt_name, filename):
        fileoutput=False
        fieldnames = ["No txn", "Date", "Compte","Montant","Commentaire"]
        with open(filename, mode="w", encoding='utf-8',newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for eachtxn in self.__transactions:
                if(eachtxn["Compte"]==accnt_name):
                    writer.writerow(eachtxn)
                    fileoutput=True
        
        if fileoutput:
            print(f"Transactions enregistrées pour le compte {accnt_name}.")
        else:
            print(f"Échec d'enregistrement des transactions pour le compte '{accnt_name}': aucune transaction ou compte pas trouvé.")

    def validate_account_name(self,account_name):
         if account_name in self.get_all_accounts():
            return True
         else:
             return False
        
         
    def handle_balance_inquiry(self):
        print("\n--- Consultation de solde ---")
        print("Comptes disponibles:")
        avail_accts=self.get_all_accounts()
        for acct in avail_accts:
            print(f"{acct}\n")
        
        account_input=None
        
        while (not account_input):

            account_input = input("\nEntrez le nom du compte: ").strip()

        if self.validate_account_name(account_input):
            balance = self.calculate_balance(account_input)
            print(f"\nSolde du compte '{account_input}': {balance:.2f}$")
        else:
            print(f"Compte '{account_input}' introuvable!")
            print("Vérifiez l'orthographe ou choisissez un compte dans la liste.")
    
    def handle_statistics(self):
        print("\n=== STATISTIQUES FINANCIÈRES ===")
        
        total_income = self.find_total_income()
        total_expenses = self.find_total_expenses()
        net_worth = total_income - total_expenses
        
        print(f"Revenus totaux: {total_income:.2f}$")
        print(f"Dépenses totales: {total_expenses:.2f}$")
        print(f"Situation nette: {net_worth:.2f}$")
        
        if net_worth > 0:
            print("📈 Situation financière positive")
        elif net_worth < 0:
            print("📉 Situation financière négative")
        else:
            print("⚖️  Situation financière équilibrée")
        
        largest_expense = self.find_largest_expense()
        
        if largest_expense:
            print(f"\nPlus grosse dépense: {float(largest_expense['Montant']):.2f}$ ({largest_expense['Compte']})")
            if largest_expense['Commentaire']:
                print(f"Commentaire: {largest_expense['Commentaire']}")
        
        current_account_balance = self.calculate_balance('Compte courant')
        print(f"\nSolde du compte courant: {current_account_balance:.2f}$")
    
    def handle_date_search(self):
        
        start_date, end_date = None, None
        while (not start_date or not end_date):
            print("\n--- Recherche par période ---")
            start_date = input("Date de début (YYYY-MM-DD): ").strip()
            end_date = input("Date de fin (YYYY-MM-DD): ").strip()
        
        filtered_data = self.get_transactions_by_date_range(start_date, end_date)
        
        if filtered_data:
            print(f"\n{len(filtered_data)} écritures(s) trouvée(s) entre {start_date} et {end_date}:")
            for eachtxn in filtered_data:
                print(f"  {eachtxn['Date']} - {eachtxn['Compte']}: {float(eachtxn['Montant']):.2f}$")
    
    def handle_export(self):
        print("\n--- Exportation ---")
        print("Comptes disponibles:")
        avail_accts=self.get_all_accounts()
        for acct in avail_accts:
            print(f"{acct}\n")
        
        account_input=None
        while(not account_input):
            account_input = input("\nEntrez le nom du compte à exporter: ").strip()
        
        validated_account = self.validate_account_name(account_input)
        
        if validated_account:
            filename = input("Nom du fichier de sortie (ex: export.csv): ").strip()
            if not filename:
                filename = f"export_{account_input}.csv".replace(' ','_')
            
            self.export_account_postings(account_input, filename)
        else:
            print(f"Compte '{account_input}' introuvable!")