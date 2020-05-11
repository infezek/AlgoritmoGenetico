from constantes import random_value, sizeCromossomo
from random import randint


class Individuo:
    def __init__(self):
        self.cromossomo = []
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = [0, 0]
        self.create()

    def create(self):
        for x in range(0, sizeCromossomo):
            rand = randint(1, 10)
            if (rand >= 5):
                self.cromossomo.append(True)
            elif (rand < 5):
                self.cromossomo.append(False)

    def getCromossomo(self):
        return self.cromossomo

    def setGene(self, position, gene):
        self.cromossomo[position] = gene

    def getGene(self, position):
        return self.cromossomo[position]

    def setFitness(self, fitness):
        self.fitness = fitness

    def getFitness(self):
        return self.fitness

    def setFitnessPercent(self, fitnessPercent):
        self.fitnessPercent = fitnessPercent

    def getFitnessPercent(self):
        return self.fitnessPercent

    def mutarBit(self, position):
        if(position < len(self.cromossomo)):
            rand = randint(1, 10)
            if (rand >= 5):
                self.cromossomo[position] = True
            elif (rand < 5):
                self.cromossomo[position] = False

    def setRangeRoleta(self, inicio, fim):
        self.faixaRoleta[0] = inicio
        self.faixaRoleta[1] = fim

    def getRangeRoleta(self):
        return self.faixaRoleta

    def getBin(self):
        value = ''
        if (len(self.cromossomo) > 32):
            pass
        for i in self.cromossomo:
            if(i):
                value = value + '1'
            else:
                value = value + '0'
        return value

    def getInt(self):
        value = ''
        if (len(self.cromossomo) > 32):
            pass
        for i in self.cromossomo:
            if(i):
                value = value + '1'
            else:
                value = value + '0'
        return int(value, 2)

    def printIndividuo(self):
        print('Cromossomo: ' + self.getBin() + ' Int: ' + str(self.getInt()) + ' Fitness: ' +
              str(self.fitness) + ' fitnessPercent: ' + str(self.fitnessPercent))


a = Individuo()
a.printIndividuo()
