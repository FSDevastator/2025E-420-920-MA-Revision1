import os
from Personal import PersonalTxn


def display_menu():
    print("\n" + "="*50)
    print("SYSTÈME DE GESTION COMPTABLE PERSONNEL")
    print("="*50)
    print("1. Afficher le solde d'un compte")
    print("2. Afficher toutes les transactions")
    print("3. Afficher les transactions d'un compte")
    print("4. Afficher le résumé de tous les comptes")
    print("5. Afficher les statistiques")
    print("6. Exporter les écritures d'un compte")
    print("7. Rechercher par période")
    print("0. Quitter")
    print("="*50)

def main():
    print("Chargement des données...")

    current=PersonalTxn()
    current.load_data('data.csv')
    
    running = True
    while running:
        display_menu()
        
        try:
            choice = input("\nVotre choix: ").strip()
        except:
            print("\nAu revoir!")
            break
        
        if choice == "1":
            current.handle_balance_inquiry()
        elif choice == "2":
            current.display_all_transactions()
        elif choice == "3":
            print("\n--- Transactions par compte ---")
            print("Comptes disponibles:")
            for each in current.get_all_accounts():
                print(f"{each}\n")
            
            account_input = input("\nEntrez le nom du compte: ").strip()

            while (not account_input):
                account_input = input("\nEntrez le nom du compte: ").strip()
            
            if account_input:
                validated_account = current.validate_account_name(account_input)
                if validated_account:
                    current.display_transactions_byaccount(account_input)
                else:
                    print(f"Compte '{account_input}' introuvable!")
            else:
                print("Nom de compte invalide!")
        elif choice == "4":
            current.display_summary()
        elif choice == "5":
            current.handle_statistics()
        elif choice == "6":
            current.handle_export()
        elif choice == "7":
            current.handle_date_search()
        elif choice == "0":
            print("\nMerci d'avoir utilisé le système de gestion comptable!")
            print("Au revoir!")
            running = False
        else:
            print("❌ Choix invalide! Veuillez sélectionner une option valide.")
        
        if running and choice != "0":
            input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()