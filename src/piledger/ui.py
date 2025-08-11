from AcctHandler import AcctHandler

class UI():

    @staticmethod
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

    @staticmethod
    def mainUI(txns):     
        running = True
        while running:
            UI.display_menu()
            
            try:
                choice = input("\nVotre choix: ").strip()
            except:
                print("\nAu revoir!")
                break
            
            if choice == "1":
                AcctHandler.handle_balance_inquiry(txns)
            elif choice == "2":
                AcctHandler.display_transactions(txns)
            elif choice == "3":
                print("\n--- Transactions par compte ---")
                print("Comptes disponibles:")
                for each in AcctHandler.get_all_accounts(txns):
                    print(f"{each}\n")
                
                account_input = input("\nEntrez le nom du compte: ").strip()

                while (not account_input):
                    account_input = input("\nEntrez le nom du compte: ").strip()
                
                if account_input:
                    validated_account = AcctHandler.validate_account_name(txns,account_input)
                    if validated_account:
                        AcctHandler.display_transactions_byaccount(txns,account_input)
                    else:
                        print(f"Compte '{account_input}' introuvable!")
                else:
                    print("Nom de compte invalide!")
            elif choice == "4":
                AcctHandler.display_summary(txns)
            elif choice == "5":
                AcctHandler.handle_statistics(txns)
            elif choice == "6":
                AcctHandler.handle_export(txns)
            elif choice == "7":
                AcctHandler.handle_date_search(txns)
            elif choice == "0":
                print("\nMerci d'avoir utilisé le système de gestion comptable!")
                print("Au revoir!")
                running = False
            else:
                print("❌ Choix invalide! Veuillez sélectionner une option valide.")
            
            if running and choice != "0":
                input("\nAppuyez sur Entrée pour continuer...")

        
        