import pandas as pd
import numpy as np
import pyAgrum as gum
import matplotlib.pyplot as plt

data = pd.read_csv("/content/asia10K (4).csv")

test_data = data[:2000]
new_data = data[2000:].copy()

learner = gum.BNLearner(test_data)
learner.useScoreBIC()
learner.useGreedyHillClimbing()
model = learner.learnBN()

bn = gum.BayesNet(model)
learner2 = gum.BNLearner(new_data, model)
learner2.useEM(1e-10)
learner2.fitParameters(bn)


plt.plot(np.arange(1, 1 + learner2.nbrIterations()))
plt.semilogy()
plt.title("Error during EM Iterations")
plt.show()
