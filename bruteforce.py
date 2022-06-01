import csv
import time
from itertools import combinations
from tqdm import tqdm

start_time = time.time()
MAX_MONEY = 500

def run():
    shares_list = get_shares_from_csv('bruteforce_test.csv')
    best_combo = shares_combos(shares_list)
    display_results(best_combo)
    results_to_csv(best_combo)
    print("Temps d'execution : %s seconds" % (time.time() - start_time))

def get_shares_from_csv(csv_file):

    shares_list = []

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        header = next(reader)
        
        for row in reader:
            shares_list.append((row[0], float(row[1]), float(row[2])))

    return shares_list

def shares_combos(shares_list):

    best_profit = 0
    best_combo = []

    for i in tqdm(range(len(shares_list))):
        combos = combinations(shares_list, i + 1)

        for combo in combos:
            total_cost = calc_total_cost(combo)

        if total_cost <= MAX_MONEY:
            profit = calc_profit(combo)

        if profit > best_profit:
            best_profit = profit
            best_combo = combo

    return best_combo

def calc_total_cost(combo):

    shares_cost = []
    for share in combo:
        shares_cost.append(share[1])

    total_cost = sum(shares_cost)

    return total_cost

def calc_profit(combo):
    total_profit = 0
    for share in combo:
        profit = share[1] * share[2] / 100
        total_profit += profit

    return total_profit

def display_results(best_combo):
    print('Meilleur investissement avec 500€ : ')

    for share in best_combo:
        print(f'{share[0]} | {share[1]} | +{share[2]} %')

    print('\nCoût des actions : ', calc_total_cost(best_combo), '€"')
    print('Profit après 2 ans : +', calc_profit(best_combo), '€\n')

def results_to_csv(best_combo):
    with open('investment.csv', 'w', newline = '', encoding = 'utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        writer.writerow(["Nom de l'action", "Prix de l'action" 'Bénéfice réalisé après 2 ans (en %)'])
        for share in best_combo:
            writer.writerow([share[0], share[1], share[2]])

    print("La meilleur combinaison d'investissement a été enregistrée dans le fichier 'investment.csv'")
    print("Pour lire ce fichier, ouvrez le à l'aide d'un tableur.\n")

if __name__ == "__main__":
    run()