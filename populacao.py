from individuo import Individuo
from constantes import function, sizePopulacao, sizeCromossomo, functrinXSize


class Populacao:
    def __init__(self):
        self.populacao = []
        for i in range(0, sizePopulacao):
            self.populacao.append(Individuo())
        self.calcularFitness()
        self.calcularFitnessPercent()
        self.calcularRangeRoleta()

    def calcularFitness(self):
        for i in range(1, sizePopulacao):
            self.populacao[i].setFitness(function(self.populacao[i].getInt()))

    def calcularFitnessPercent(self):
        somatoriaFitness = 0
        for i in range(0, sizePopulacao):
            somatoriaFitness += self.populacao[i].getFitness()

        for i in range(0, sizePopulacao):
            self.populacao[i].setFitnessPercent(
                (self.populacao[i].getFitness() * 100) / somatoriaFitness)

    def calcularRangeRoleta(self):
        self.OrdenarPopulacao()
        somatoria = 0
        for i in range(0, sizePopulacao):
            if(i == 0):
                somatoria += self.populacao[i].getFitnessPercent()
                self.populacao[i].setRangeRoleta(0, somatoria)
            elif(i == (sizePopulacao - 1)):
                self.populacao[i].setRangeRoleta(somatoria, 100)
            else:
                self.populacao[i].setRangeRoleta(
                    somatoria, somatoria + self.populacao[i].getFitnessPercent())
                somatoria += self.populacao[i].getFitnessPercent()

    def atuazarValores(self):
        self.calcularFitness()
        self.calcularFitnessPercent()
        self.calcularRangeRoleta()

    def getPopulacao(self):
        return self.populacao

    def setIndividuo(self, posicao, individuo):
        self.populacao[posicao] = individuo

    def getMediaPopulacao(self):
        sum = 0
        for i in self.populacao:
            sum += i.getFitness()
        return int(sum / sizePopulacao)

    def OrdenarPopulacao(self):
        aux = Individuo()
        for i in range(0, sizePopulacao):
            for j in range(0, sizePopulacao):
                if (self.populacao[i].getFitnessPercent() < self.populacao[j].getFitnessPercent()):
                    aux = self.populacao[i]
                    self.populacao[i] = self.populacao[j]
                    self.populacao[j] = aux

    def printPop(self):
        resultado = ''
        for i in range(0, sizeCromossomo):
            resultado += ('Cromossomo: ' + self.populacao[i].getBin() + ' Int: ' + str(self.populacao[i].getInt(
            )) + ' Fitness: ' + str(self.populacao[i].fitness) + ' fitnessPercent: ' + str(self.populacao[i].fitnessPercent)) + '\n'

        return resultado
    

b = Populacao()
b.getPopulacao()
