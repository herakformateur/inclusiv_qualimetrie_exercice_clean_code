class SortList:       
    
    def __init__(self) :
        self.current_list= []
        inputSuiteNombre = input("Entrer une suite de nombre séparé par un virgule: ")
        self.current_list=inputSuiteNombre.split(",")  
        self.affichelisteTrieravecChoix()                
    
    def affichelisteTrieravecChoix(self):
        choix_utilisateur=input("-----------------------\n Veuillez faire votre choix d'ordre (0 pour croissant, 1 pour décroissant)\n Votre Choix :")
        if choix_utilisateur=="0":
            print(sorted(self.current_list))
        elif choix_utilisateur=="1":
            print(sorted(self.current_list,reverse=True))
        else:
            print("Erreur")
            self.affichelisteTrieravecChoix()
    
    def sortListAscending(self):
        print(sorted(self.current_list))
        return sorted(self.current_list)
        
    def sortListDescending(self):
        print(sorted(self.current_list, reverse=True))
        return sorted(self.current_list, reverse=True)
    
    
    