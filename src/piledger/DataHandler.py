import csv
import os
from pathlib import Path
from Txn_General import GeneralTxn

class DataHandler():

    @staticmethod
    def load(file='data.csv'):
        '''Recherche dans tous les dossiers du projet pour le fichier à charger.
           Retourne un objet contenant une transaction
        '''
        base_path=os.getcwd()
        search_path=Path(base_path)
        search_path=search_path / file
  
        txns=[]
        
        found_file=False

        print("Chargement des données...")

        try:
            
            while(found_file==False):
                if (search_path.exists()):
                    with open(search_path,'r', encoding='utf-8') as file:
                        reader=csv.DictReader(file)
                        for row in reader:
                            
                            txns.append(
                                
                                GeneralTxn(
                                    int(row['No txn']),
                                        row['Date'],
                                        row['Compte'],
                                        float(row['Montant']),
                                        row['Commentaire'])
                            )
                    found_file=True
                    
                    if not txns:
                        print(f"Fichier {file} ne contient pas de transactions.  Aucunes données chargées.")
                    elif txns:
                        print(f"Données chargées avec succès.")
                                        
                else:
                    search_path=search_path.parent
                    if ((search_path/'pyproject.toml').exists()):
                        raise FileNotFoundError
                    search_path=search_path.parent
                    search_path=search_path/str(file)              
        
        except FileNotFoundError as e:
            print(f"Erreur: fichier {e} introuvable.")
        
        return txns