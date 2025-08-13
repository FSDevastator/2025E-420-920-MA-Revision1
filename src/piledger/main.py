from DataHandler import DataHandler
from AcctHandler import AcctHandler
from ui import UI

def main():

    txns=DataHandler.load()
    UI.mainUI(txns)

if __name__ == "__main__":
    main()