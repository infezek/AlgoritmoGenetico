from individuo import Individuo
from populacao import Populacao
from constantes import function, sizePopulacao, sizeCromossomo, functrinXSize, random_value
import matplotlib.pyplot as plt


class AlgoritmoGenetico:
    def __init__(self, populacao, taxaCrossover, taxaMutacao):
        self.taxaCrossover = taxaCrossover
        self.taxaMutacao = taxaMutacao
        self.PAI = 0
        self.MAE = 1
        self.populacao = populacao

    def executaAG(self):
        novaPopulacao = Populacao()
        popBuffer = []
        for i in range(0, int(sizePopulacao/2)):
            pai = self.Roleta(self.populacao)
            mae = self.Roleta(self.populacao)
            filhos = self.Crossover(pai, mae)

            filhoA = self.Mutacao(filhos[0])
            filhoB = self.Mutacao(filhos[1])
            popBuffer.append(filhoA)
            popBuffer.append(filhoB)

        for i in range(0, sizePopulacao):
            novaPopulacao.setIndividuo(i, popBuffer[i])
        popBuffer = ''
        novaPopulacao.atuazarValores()

        return novaPopulacao

    def Crossover(self, pai, mae):
        novoInd = [0, 0]
        pontoDeCorte = random_value(0, sizeCromossomo)
        paiBuffer = Individuo()
        maeBuffer = Individuo()
        novoInd[self.PAI] = Individuo()
        novoInd[self.MAE] = Individuo()

        for i in range(0, sizeCromossomo):
            paiBuffer.setGene(i, pai.getGene(i))
            maeBuffer.setGene(i, mae.getGene(i))
            novoInd[self.PAI].setGene(i, pai.getGene(i))
            novoInd[self.MAE].setGene(i, mae.getGene(i))

        if(random_value(0, 10) < self.taxaCrossover):
            for i in range(pontoDeCorte, sizeCromossomo):
                novoInd[self.PAI].setGene(i, maeBuffer.getGene(i))
                novoInd[self.MAE].setGene(i, paiBuffer.getGene(i))
        return novoInd

    def Mutacao(self, ind):
        if(random_value(0, sizeCromossomo) <= self.taxaMutacao):
            genePosition = random_value(0, sizeCromossomo)
            ind.mutarBit(genePosition)
            return ind
        return ind

    def Roleta(self, pop):
        numSorteado = random_value(0, 100)
        for ind in pop.getPopulacao():
            if(numSorteado >= ind.getRangeRoleta()[0] and numSorteado <= ind.getRangeRoleta()[1]):
                return ind
        pass

    def printPopulacao(self):
        print(self.populacao.printPop())

    def getPopulacao(self):
        return self.populacao


poppp = Populacao()
mat = []
for i in range(0, sizePopulacao):
    a = AlgoritmoGenetico(poppp, 0.2, 0.2)
    poppp = a.getPopulacao()


b = poppp.getPopulacao()
x = []
y = []
for i in range(0, sizePopulacao):
    valueInt = b[i].getInt()
    mat.append(function(i))
    x.append(function(valueInt))
    y.append(valueInt)

plt.scatter(y, x, label='Pontos', color='r', marker='.', s=20)
plt.legend()

plt.plot(mat)
plt.show()
a.printPopulacao()
