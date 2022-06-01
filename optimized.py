import csv
import time
import os.path
from os import path
from operator import itemgetter



def run():
    data_file = ask_data_file()
    start_time = time.time()
    shares_list = get_shares_from_csv(data_file)
    best_combo = knapsack(shares_list)
    display_results(best_combo)
    results_to_csv(best_combo, data_file)
    print("Temps d'execution : %s seconds" % (time.time() - start_time))

def ask_data_file():
    
    while True:
        data_file = input('Entrez le nom du fichier csv à analyser (ex: bruteforce_test) : ')
        data_file += '.csv'
        print(f'Fichier recherché : {data_file}')
        valid_file = path.exists(data_file)
        if valid_file:
            return data_file
        else:
            print('Fichier non existant.')


def get_shares_from_csv(csv_file):
    shares_list = []

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        header = next(reader)
        
        for row in reader:
            shares_list.append([row[0], float(row[1]), float(row[2])])
    sorted_shares_list = sorted(shares_list, key=itemgetter(2), reverse=True)
    return sorted_shares_list

def knapsack(shares_list):
    """Résolution par algorithme glouton"""
    MONEY = 500
    best_combo = []
    for share in shares_list:
        if MONEY > share[1] >= 0:
            best_combo.append(share)
            MONEY -= share[1]
        elif MONEY == 0:
            break
    return best_combo

def calc_total_cost(best_combo):

    total_cost = 0
    for share in best_combo:
        total_cost += share[1]

    return total_cost

def calc_profit(best_combo):
    total_profit = 0
    for share in best_combo:
        profit = share[1] * share[2] / 100
        total_profit += profit

    return total_profit

def display_results(best_combo):
    print('Meilleur investissement avec 500€ : ')

    for share in best_combo:
        print(f'{share[0]} | {share[1]} | +{share[2]} %')

    print(f'\nCoût des actions : {round(calc_total_cost(best_combo), 2)}€')
    print(f'Profit après 2 ans : + {round(calc_profit(best_combo), 2)}€\n')

def results_to_csv(best_combo, data_file):
    data_file = data_file.replace('.csv', '')
    print(data_file)
    with open(data_file + '_investment.csv', 'w', newline = '', encoding = 'utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        writer.writerow(["Nom de l'action", "Prix de l'action" 'Bénéfice réalisé après 2 ans (en %)'])
        for share in best_combo:
            writer.writerow([share[0], share[1], share[2]])

    print(f"La meilleur combinaison d'investissement a été enregistrée dans le fichier '{data_file}_investment.csv'")
    print("Pour lire ce fichier, ouvrez le à l'aide d'un tableur.\n")

if __name__ == '__main__':
    run()