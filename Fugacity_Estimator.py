import numpy as np
import math as m

Data_Table = {
    "Argon" : [150.86, 48.98, -0.002, 6.43, 0, 29.10, 90.00],
    "Tetrachloromethane" : [556.3, 45.57, 0.194, 29.82, 3.28, 97.07, 298.15],
    "Tetrafluoromethane" : [227.51, 37.45, 0.177, 0, 0, 56.41, 153.15],
    "Chlorodifluoromethane" : [369.28, 49.86, 0.221, 20.22, 4.12, 59.08, 213.15],
    "Trichloromethane" : [536.50, 55.00, 0.216, 29.24, 8.80, 80.68, 298.15],
    "Methane" : [190.56, 45.99, 0.011, 8.17, 0.94, 35.54, 90.68],
    "Methanol" : [512.64, 80.97, 0.565, 35.21, 3.18, 40.73, 298.15],
    "Carbon Monoxide" : [132.85, 34.94, 0.045, 6.04, 0.84, 34.88, 81.00],
    "Carbon Dioxide" : [304.12, 73.74, 0.225, 0, 9.02, 0, 0],
    "Pentafluoroethane" : [339.17, 36.15, 0.305, 0, 0, 98.61, 293.48],
    "Ethyne" : [308.30, 61.14, 0.189, 0, 21.28, 43.47, 203.15],
    "1,1,1-Trifluoroethane" : [346.30, 37.92, 0.259, 18.99, 6.19, 75.38, 245.00],
    "Acetonitrile" : [545.5, 48.33, 0.353, 0, 0, 0, 0],
    "Ethene" : [282.34, 50.41, 0.087, 13.53, 3.35, 51.07, 183.15],
    "1,2-Dichloroethane" : [523.00, 51.00, 0, 28.85, 7.87, 84.73, 298.15],
    "Ethane" : [305.32, 48.72, 0.099, 14.70, 2.86, 46.15, 90.36],
    "Ethanol" : [513.92, 61.48, 0.649, 38.56, 5.01, 58.68, 298.15],
    "Propene" : [364.90, 46.00, 0.142, 18.42, 3.00, 0, 0],
    "Propanone" : [508.10, 47.00, 0.307, 29.10, 5.69, 73.94, 298.15],
    "Dimethylcarbonate" : [557.00, 48.00, 0.336, 37.70, 0, 84.82, 298.15],
    "Propane" : [369.83, 42.48, 0.152, 19.04, 3.53, 74.87, 233.15],
    "1-Propanol" : [536.78, 51.75, 0.629, 41.44, 5.20, 75.14, 298.15],
    "2-Propanol" : [508.30, 47.62, 0.665, 39.85, 5.38, 76.92, 298.15],
    "1,3-Butadiene" : [425.00,43.20,0.195,22.47,7.98,88.04,298.15],
    "1-Butene" : [419.50,40.20,0.194,22.07,3.96,95.34,298.15],
    "Butanone" : [536.80,42.10,0.322,31.30,8.44,90.13,298.15],
    "n-Butane" : [425.12,37.96,0.200,22.44,4.66,100.48,298.15],
    "2-Methylpropane" : [407.85,36.40,0.186,21.30,4.61,104.36,298.15],
    "1-Butanol" : [563.05,44.23,0.590,43.29,9.28,91.96,298.15],
    "Diethyl ether" : [466.70,36.40,0.281,26.52,7.27,104.75,298.15],
    "n-Pentane" : [469.70,33.70,0.252,25.79,8.40,115.22,298.15],
    "Butyl methyl ether" : [512.8,33.71,0.316,0,0,0,0],
    "Hexafluorobenzene" : [516.73,32.75,0.396,31.66,0,0,0],
    "Chlorobenzene" : [632.40,45.20,0.251,35.19,9.61,102.22,298.15],
    "Benzene" : [562.05,48.95,0.210,30.72,9.95,89.41,298.15],
    "Phenol" : [694.25,61.30,0.442,46.18,11.29,87.87,298.15],
    "Cyclohexane" : [553.50,40.73,0.211,29.97,2.63,108.75,298.15],
    "1-Hexene" : [504.00,31.43,0.281,28.28,7.52,125.90,298.15],
    "n-Hexane" : [507.60,30.25,0.300,28.85,13.07,131.59,298.15],
    "Toluene" : [591.75,41.08,0.264,33.18,6.85,106.87,298.15],
    "n-Heptane" : [540.20,27.40,0.350,31.77,14.03,147.47,298.15],
    "Ethylbenzene" : [617.15,36.09,0.304,35.57,9.18,123.08,298.15],
    "o-Xylene" : [630.30,37.32,0.312,36.24,13.60,121.25,298.15],
    "m-Xylene" : [617.00,35.41,0.327,35.66,11.57,123.47,298.15],
    "p-Xylene" : [616.20,35.11,0.322,35.67,16.81,123.93,298.15],
    "n-Octane" : [568.70,24.90,0.399,34.41,20.65,163.53,298.15],
    "n-Nonane" : [594.60,22.90,0.445,36.91,15.50,179.70,298.15],
    "Naphthalene" : [748.40,40.50,0.304,43.40,19.12,129.13,333.15],
    "n-Decane" : [617.70,21.10,0.490,38.75,28.78,195.95,298.15],
    "Chlorine" : [417.00,77.00,0.069,20.41,0,45.36,239.00],
    "Hydrogen" : [33.25,12.97,-0.216,0.89,0.12,29.39,20.00],
    "Water" : [647.14,220.64,0.344,40.66,6.01,18.07,298.15],
    "Nitrogen" : [126.2,33.98,0.037,5.58,0.72,34.84,78.00],
    "Ammonia" : [406.6,112.7,0.252,0,0,25.0,240.0],
    "Oxygen" : [154.58,50.43,0.022,6.82,0.44,27.85,90.00],
}

entry = input("Enter the name of the compound: ")

compound_data = Data_Table.get(entry)
if compound_data is None:
    print("Compound not found in the data table.")
    exit()

print(f"Compound: {entry}")
print(f"Critical Temperature (K): {compound_data[0]}")
print(f"Critical Pressure (bar): {compound_data[1]}")
print(f"Eccentric Factor: {compound_data[2]}")
print(f"Enthalpy of Vaporization (kJ/mol): {compound_data[3]}")
print(f"Enthalpy of Fusion (kJ/mol): {compound_data[4]}")
print(f"Liquid Molar Volume (cm^3/mol): {compound_data[5]}")
print(f"Temperature for Volume Data (K): {compound_data[6]}")


Tin = float(input("Enter the temperature (K): "))
Tc = compound_data[0]
Pc = compound_data[1]
w = compound_data[2]
Hv = compound_data[3]
Hf = compound_data[4]
Vl = compound_data[5]
Tv = compound_data[6]
Rc = 0.08314462618
b = 0.0777960739 * (Rc * Tc / Pc)
a = 0.4572355289 * ((Rc ** 2) * (Tc ** 2) / Pc)
alpha = (1 + (0.37464 + 1.54226 * w - 0.26992 * (w ** 2)) * (1 - (Tin / Tc) ** 0.5)) ** 2
at = a * alpha

Pguess = float(input("Enter the intial pressure (bar) guess: "))

fugacity_liquid_guess = 1
fugacity_vapor_guess = 1
fugacity_diff = 1



def coefficients(A, B):
    c1 = 1
    c2 = -(1 - B)
    c3 = A - 3 * (B ** 2) - 2 * B
    c4 = -(A * B - (B ** 2) - (B ** 3))

    coefficients = [c1, c2, c3, c4]

    return coefficients

def fugacity_coefficient(Z, A, B):
    if (Z - B) <= 0:
        return np.nan
        
    num = Z + (1 + np.sqrt(2)) * B
    den = Z + (1 - np.sqrt(2)) * B
    if (num / den) <= 0:
        return np.nan

    ln_phi = Z - 1 - np.log(Z - B) - (A / (2 * np.sqrt(2) * B)) * np.log(num / den)
    return np.exp(ln_phi)

def fugacity(P):
    B1 = b * P / (Rc * Tin)
    A1 = at * P / ((Rc ** 2) * (Tin ** 2))
    Z_roots = np.roots(coefficients(A1, B1))
    Z_roots = [root.real for root in Z_roots if np.isreal(root)]
    Z_roots.sort()

    if len(Z_roots) == 1:
        fugacity_liquid_guess = fugacity_coefficient(Z_roots[0], A1, B1)
        fugacity_vapor_guess = None
        fugacity_diff = None
    elif len(Z_roots) == 3:
        fugacity_liquid_guess = fugacity_coefficient(Z_roots[0], A1, B1)
        fugacity_vapor_guess = fugacity_coefficient(Z_roots[2], A1, B1)
        fugacity_diff = float(abs(fugacity_liquid_guess - fugacity_vapor_guess))
    else:
        print("Unexpected number of roots found. Cannot estimate fugacity.")

    return fugacity_liquid_guess, fugacity_vapor_guess, fugacity_diff, A1, B1, Z_roots

estimate = input("Do you want to estimate the equilibrium pressure? (y/n): ")

if estimate == "y":
    fugacity_liquid_guess, fugacity_vapor_guess, fugacity_diff, A1, B1, Z_roots = fugacity(Pguess)
    if len(Z_roots) == 1:
        print("Only one root found. Cannot estimate equilibrium pressure.")
    else:
        for i in range(100):
            fugacity_liquid_guess, fugacity_vapor_guess, fugacity_diff, A1, B1, Z_roots = fugacity(Pguess)
            if fugacity_diff < 1e-9:
                break
            else:
                Pguess = Pguess * (fugacity_liquid_guess / fugacity_vapor_guess)**0.5
else:
    fugacity_liquid_guess, fugacity_vapor_guess, fugacity_diff, A1, B1, Z_roots = fugacity(Pguess)

print("\n--- Peng-Robinson Results ---")
print(f"Final Pressure: {Pguess:.5f} bar")
print(f"Liquid Fugacity Coefficient: {fugacity_liquid_guess:.6f}")

if fugacity_vapor_guess is not None:
    print(f"Vapor Fugacity Coefficient: {fugacity_vapor_guess:.6f}")
    print(f"Liquid Fugacity: {fugacity_liquid_guess * Pguess:.5f} bar")
    print(f"Vapor Fugacity: {fugacity_vapor_guess * Pguess:.5f} bar")

print(f"A = {A1:.6f}")
print(f"B = {B1:.6f}")
print(f"Liquid Z = {Z_roots[0]:.6f}")
print(f"Vapor Z = {Z_roots[-1]:.6f}")
