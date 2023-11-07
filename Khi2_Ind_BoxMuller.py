import numpy as np
from scipy.stats import chi2_contingency

# ______________ HYPOTHESIS TESTING ______________ 
# H0 = randoms variables X and Y are independants
# H1 = randoms variables X and Y are not independants



#number of randoms values
N = 1000

#create sample of uniform distribution
U1 = np.random.uniform(0,1,N)
U2 = np.random.uniform(0,1,N)

#create sample of gaussien distribution N(0,1) by Box-Muller transform
x = np.sqrt(-2.0*np.log(U1))*np.cos(2.0*np.pi*U2)
y = np.sqrt(-2.0*np.log(U1))*np.sin(2.0*np.pi*U2)


# number of class for independancy Khi2 test
k = 10

#to avoid problem in extremities (a random value equal to an extremity)
epsilon = 1e-3

#create interval
x_bins = np.linspace(x.min()-epsilon, x.max()+epsilon, k+1)
y_bins = np.linspace(y.min()-epsilon, y.max()+epsilon, k+1)

#renvoie un tableau d'incide, chaque indice i correpond à la classe au quel apprtient la valeur x du tableau
x_digitized = np.digitize(x, x_bins) - 1

y_digitized = np.digitize(y, y_bins) - 1

#init du tableau de contingence
contingency_table = np.zeros((k, k), dtype=int)

#on range les valeurs
for i in range(N):
    contingency_table[x_digitized[i], y_digitized[i]] += 1

print(contingency_table)



# Utilisez la fonction chi2_contingency de SciPy pour effectuer le test
chi2, p, _, expected = chi2_contingency(contingency_table)

print("Valeur de chi2:", chi2)
print("Valeur p:", p)

# Décidez si les variables sont indépendantes ou non en fonction de la valeur p
alpha = 0.05
if p < alpha:
    print("Rejet de l'hypothèse nulle : les variables ne sont pas indépendantes.")
else:
    print("Acceptation de l'hypothèse nulle : les variables sont indépendantes.")