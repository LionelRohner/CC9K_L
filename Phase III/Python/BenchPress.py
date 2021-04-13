import pandas as pd
import timeit as tmt
import matplotlib.pyplot as plt
import os


class BenchPress:

    def __init__(self, data, benchMeth):

        # create result Pandas
        self.res = pd.DataFrame(data)
        self.benchMeth = benchMeth

    def getDaReps(self, algo, algoN, nIter = None):


        if self.benchMeth == "Nenad":
            if nIter == None:
                nIter = 100

            tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
            self.res[algoN] = tst
            print()
        else:
            if nIter == None:
                nIter = 5000
            elapsed_time = tmt.timeit(algo, number=nIter)
            print(algoN, ": ", elapsed_time / nIter)
            self.res[algoN] = [elapsed_time]
            print("Loop Done.")
            print()

    def plotBP(self):

        # depending on the method show propagation, i.e. the Nenadian Plot
        if self.benchMeth == "Nenad":
            self.res.plot(ylim=[min(self.res.min()), max(self.res.max())])

        # Crappy boxplot, whose ylim makes you want to jump out of the window
        else:
            self.res.boxplot()

        plt.show()



    def returnRes(self):
        return(self.res)

    def saveCSV(self, outName = '\\res.csv'):
            self.res.to_csv(os.getcwd() + outName)