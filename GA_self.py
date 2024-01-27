import numpy as np
import random
import matplotlib.pyplot as plt

a = np.random.randint(0, 50, (1, 3))
inheritedIndividual = 70

coefficient = np.array([3, 4, 5])

right = 100
maxSize = 100

# 确定问题的方程
def calFunction(coefficient,individual):
    # X^2+3y-z<1024:
    if individual.ndim==1:
        individual=individual[np.newaxis,:]
    if coefficient.shape==(1,3):
        coefficient=coefficient[:,np.newaxis]
    temp=np.array(individual[:,0])
    temp=temp **2
    individual[:,0]=temp
    if np.dot(individual,coefficient)<1024:
        return True
    else:
        return False

# 随机生成初始解
def generate(coefficient, maxSize):
    individual = np.array([[1, 1, 1]])
    while np.size(individual, 0) < maxSize:
        ans = np.random.randint(0, 50, (1, 3))
        if calFunction(coefficient,ans)==True:
            individual = np.vstack((individual, ans))
    return individual


# 计算适应度
# 这里采用的计算方法是三个解简单相加
def calFitness(individuals):
    fitness = []
    for ind in individuals:
        fitness.append(sum(ind))
    return fitness


#适应度高的解遗传给下一代
def inheritance(individuals, sort):
    new_individuals = []
    i = 0
    while i < inheritedIndividual:
        new_individuals.append(individuals[sort[maxSize - i - 1]])
        i = i + 1
    return new_individuals


# 随机产生变异
def variance(individuals, new_individuals):
    while np.size(new_individuals, 0) < maxSize:
        i = random.randint(0, maxSize - 1)
        ind = individuals[i]
        ind=list(ind)
        a = ind[0] + random.randint(-5, 5)
        b = ind[1] + random.randint(-5, 5)
        c = ind[2] + random.randint(-5, 5)
        if a >= 0:
            ind[0] = a
        if b >= 0:
            ind[1] = b
        if c >= 0:
            ind[2] = c
        ind=np.array(ind)
        if calFunction(coefficient,ind):
            new_individuals = np.vstack((new_individuals, ind))
    return new_individuals


def main():
    individual = generate(coefficient, maxSize)
    print(individual.shape)
    print(individual)
    fitness = calFitness(individual)
    sort = np.argsort(fitness)
    circle = 1
    print(max(fitness))
    max_fit = [max(fitness)]
    while max(fitness) < 6000 and circle < 5000:
        circle = circle + 1
        new_individuals = inheritance(individual, sort)
        temp_individual = variance(individual, new_individuals)  # 一代进化后的个体
        fitness_new = calFitness(temp_individual)  # 进化后的适应度
        if max(fitness_new) < max(fitness):
            temp_individual = individual  # 不如原来的就不进化
            fitness_new = fitness
        # individual = np.array(individual)
        max_fit.append(max(fitness_new))
        sort = np.argsort(fitness_new)
        individual = temp_individual
        fitness = fitness_new
        print(f"when in circle: {circle}, the max fitness is {max(fitness_new)},the individuals are {individual[sort[99]]}")

    plt.plot(max_fit)
    plt.show()

main()