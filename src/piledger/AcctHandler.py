
import csv
from datetime import datetime 

class AcctHandler():

    @staticmethod
    def calculate_balance(txns, acctname):
        return sum([eachtxn.amount for eachtxn in txns if eachtxn.account==acctname])
    
    @staticmethod
    def get_all_accounts(txns):
        return set([eachtxn.account for eachtxn in txns])

    @staticmethod
    def display_transactions(txns):
        for eachtxn in txns:
            print(eachtxn)
    
    @staticmethod
    def display_transactions_byaccount(txns,acctname):

        print(f"Transactions pour le compte '{acctname}':\n")
        
        result=[eachtxn for eachtxn in txns if eachtxn.account==acctname]
        for eachtxn in result:
            print(eachtxn)
            print()
        
        if result:
             print(f"{len(result)} transaction(s) trouvée(s) pour le compte {acctname}\n")
        else:
            print(f"Aucune transaction trouvée pour le compte {acctname}.\n")
    
    @staticmethod
    def display_summary(txns):
        print("\n=== RÉSUMÉ DES COMPTES ===")
        accounts= AcctHandler.get_all_accounts(txns)

        for acct in accounts:
            balance=AcctHandler.calculate_balance(txns,acct)
            print(f"{acct}: {balance}$")

    @staticmethod
    def get_transactions_by_date_range(txns, start_date, end_date):
            valid_txns=[]
            date_format="%Y-%m-%d"

            for eachtxn in txns:
                if (datetime.strptime(eachtxn.date,
                                date_format)).date() >= (datetime.strptime(start_date,date_format)).date():
                    if (datetime.strptime(eachtxn.date,
                                date_format)).date() <= (datetime.strptime(end_date,date_format)).date():
                    
                        valid_txns.append(eachtxn)
            
            if (valid_txns):
                return valid_txns 
            else: 
                print(f"Aucune transaction entre {start_date} et {end_date}.")
                return valid_txns
        
    @staticmethod
    def find_largest_expense(txns):
        filtered_expenses= [eachtxn for eachtxn in txns if eachtxn.account!='Revenu' and eachtxn.account!='Compte courant']
        return sorted(filtered_expenses, key=lambda x: x.amount, reverse=True).pop(0)
    
    @staticmethod
    def find_total_income(txns):
        return abs(AcctHandler.calculate_balance(txns,'Revenu'))
    
    @staticmethod
    def find_total_expenses(txns):
        filtered_expenses= [eachtxn for eachtxn in txns if eachtxn.account!='Revenu' and eachtxn.account!='Compte courant']
        return sum([eachtxn.amount for eachtxn in filtered_expenses])
    
    @staticmethod
    def export_account_postings(txns, accnt_name, filename):
        fileoutput=False
        fieldnames = ["No txn", "Date", "Compte","Montant","Commentaire"]
        with open(filename, mode="w", encoding='utf-8',newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for eachtxn in txns:
                if(eachtxn.account==accnt_name):
                    writer.writerow(eachtxn)
                    fileoutput=True

        if fileoutput:
            print(f"Transactions enregistrées pour le compte {accnt_name}.")
        else:
            print(f"Échec d'enregistrement des transactions pour le compte '{accnt_name}': aucune transaction ou compte pas trouvé.")

    @staticmethod
    def validate_account_name(txns,account_name):
            return True if account_name in AcctHandler.get_all_accounts(txns) else False
                      
    @staticmethod     
    def handle_balance_inquiry(txns):
        print("\n--- Consultation de solde ---")
        print("Comptes disponibles:")
        avail_accts=AcctHandler.get_all_accounts(txns)
        for acct in avail_accts:
            print(f"{acct}\n")
        
        account_input=None
        
        while (not account_input):

            account_input = input("\nEntrez le nom du compte: ").strip()

        if AcctHandler.validate_account_name(txns,account_input):
            balance = AcctHandler.calculate_balance(txns,account_input)
            print(f"\nSolde du compte '{account_input}': {balance}$")
        else:
            print(f"Compte '{account_input}' introuvable!")
            print("Vérifiez l'orthographe ou choisissez un compte dans la liste.")
    
    @staticmethod
    def handle_statistics(txns):
        print("\n=== STATISTIQUES FINANCIÈRES ===")
        
        total_income = AcctHandler.find_total_income(txns)
        total_expenses = AcctHandler.find_total_expenses(txns)
        net_worth = total_income - total_expenses
        
        print(f"Revenus totaux: {total_income}$")
        print(f"Dépenses totales: {total_expenses}$")
        print(f"Situation nette: {net_worth}$")
        
        if net_worth > 0:
            print("📈 Situation financière positive")
        elif net_worth < 0:
            print("📉 Situation financière négative")
        else:
            print("⚖️  Situation financière équilibrée")
        
        largest_expense = AcctHandler.find_largest_expense(txns)
        
        if largest_expense:
            print(f"\nPlus grosse dépense: {largest_expense.amount}$ ({largest_expense.account})")
            if largest_expense.comment:
                print(f"Commentaire: {largest_expense.comment}")
        
        current_account_balance = AcctHandler.calculate_balance(txns,'Compte courant')
        print(f"\nSolde du compte courant: {current_account_balance}$")
    
    @staticmethod
    def handle_date_search(txns):
        
        start_date, end_date = None, None
        while (not start_date or not end_date):
            print("\n--- Recherche par période ---")
            start_date = input("Date de début (YYYY-MM-DD): ").strip()
            end_date = input("Date de fin (YYYY-MM-DD): ").strip()
        
        filtered_data = AcctHandler.get_transactions_by_date_range(txns,start_date, end_date)
        
        if filtered_data:
            print(f"\n{len(filtered_data)} écritures(s) trouvée(s) entre {start_date} et {end_date}:")
            for eachtxn in filtered_data:
                print(f"  {eachtxn.date} - {eachtxn.account}: {eachtxn.amount:.2f}$")
    
    @staticmethod
    def handle_export(txns):
        print("\n--- Exportation ---")
        print("Comptes disponibles:")
        avail_accts=AcctHandler.get_all_accounts(txns)
        for acct in avail_accts:
            print(f"{acct}\n")
        
        account_input=None
        while(not account_input):
            account_input = input("\nEntrez le nom du compte à exporter: ").strip()
        
        validated_account = AcctHandler.validate_account_name(txns,account_input)
        
        if validated_account:
            filename = input("Nom du fichier de sortie (ex: export.csv): ").strip()
            if not filename:
                filename = f"export_{account_input}.csv".replace(' ','_')
            
            AcctHandler.export_account_postings(txns,account_input,filename)
        else:
            print(f"Compte '{account_input}' introuvable!")