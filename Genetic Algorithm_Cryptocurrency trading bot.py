import random

# Input
population = []

capital = float(input("Input Capital to Start With: "))
prices = input("Input historical prices (comma-separated): ")
historical_prices = [float(price) for price in prices.split(",")]
for i in range (4):
    genes = input(f"Enter chromosome {i+1}: (e.g. stop_loss,take_profit,trade_size) (comma-separated): ")
    chromosome = [float(g) for g in genes.split(",")]
    population.append(chromosome)

generations = input("Input number of generations: ")


# Fitness Function
def fitness(chromosome, historical_prices, initial_capital):
    capital = initial_capital
    for i in range (len(historical_prices)):
        invest = (capital * chromosome[2])/100

        change = historical_prices[i]   
        if(change <= chromosome[0]*-1):
            capital = capital - (invest * change/100) 
        elif(change >= chromosome[1]):
            capital = capital + (invest * change/100)
        else:
            capital = capital + (invest * change/100)

    fitness_value = capital - initial_capital

    return fitness_value

for generation in range (int(generations)):
  
    population.sort(
        key = lambda chromosome: fitness(
            chromosome, historical_prices, capital
        ),
        reverse = True
    )

    child_1 = population[0]
    child_2 = population[1]

    #Cross over
    offSpring_1 = [child_1[0], child_2[1], child_1[2]]
    offSpring_2 = [child_2[0], child_1[1], child_2[2]]

    #Mutation
    mutaion_rate = .05
    r = random.random()

    if r < mutaion_rate:
        offSpring_1[2] = offSpring_1[2] + random.uniform(-5, 5) 
        offSpring_2[2] = offSpring_2[2] + random.uniform(-5, 5)

        offSpring_1[0] = offSpring_1[0] + random.uniform(-.05, .05) 
        offSpring_2[0] = offSpring_2[0] + random.uniform(-.05, .05)

        offSpring_1[1] = offSpring_1[1] + random.uniform(-.05, .05) 
        offSpring_2[1] = offSpring_2[1] + random.uniform(-.05, .05)

    population[2] = offSpring_1
    population[3] = offSpring_2

population.sort(
    key = lambda chromosome: fitness(
        chromosome, historical_prices, capital
    ),
    reverse = True
 )

best = population[0]
final_profit = fitness(best, historical_prices, capital)

print("\nBest Chromosome : " , best)
print("Final Profit : " , final_profit)
