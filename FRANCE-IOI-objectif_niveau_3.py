nbLivres, nbJours = map(int, input().strip().split())
bibliotheque=list(range(nbLivres))
clients=[]

def visiter(bibliotheque,clients):
    bibliotheque=ajouter(bibliotheque,clients)
    bibliotheque=retirer(bibliotheque,clients)
    return bibliotheque

def ajouter(bibliotheque,clients):
    aujourdhui=len(clients)
    for (jour,clients_aujourdhui) in enumerate(clients):
        for client in clients_aujourdhui:
            indice, duree = client
            if jour+duree == aujourdhui:
                bibliotheque.append(indice)
    return bibliotheque

def retirer(bibliotheque, clients):
    for client in clients[-1]:
        indice = client[0]
        if indice in bibliotheque:
            bibliotheque.remove(indice)
            print(1)
        else:
            print(0)
    return bibliotheque

for _ in range(1, nbJours + 1):
    nbClients = int(input().strip())
    nouveaux_clients=[]
    for _ in range(0, nbClients):
        indice, duree = map(int, input().strip().split()) 
        nouveaux_clients.append([indice, duree])
    clients.append(nouveaux_clients)
    bibliotheque=visiter(bibliotheque,clients)
