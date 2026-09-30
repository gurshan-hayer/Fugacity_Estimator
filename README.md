# Fugacity Estimator

A Python-based thermodynamic modeling program that uses the Peng-Robinson equation of state (PR EOS) to calculate fugacity coefficients, fugacity, compressibility factors, and estimate vapor-liquid equilibrium pressure.

## Overview

This project implements a computational workflow for analyzing real-fluid behavior using the Peng-Robinson equation of state.

The program allows the user to:

- Select a compound from a built-in thermodynamic property database
- Enter a temperature and initial pressure guess
- Calculate Peng-Robinson EOS parameters
- Solve the cubic EOS for compressibility factor (`Z`) roots
- Calculate liquid and vapor fugacity coefficients
- Calculate liquid and vapor fugacity
- Estimate equilibrium pressure by iterating toward equal liquid and vapor fugacity
- Add additional compounds to the thermodynamic property database

Thermodynamic Model

The program uses the Peng-Robinson equation of state to account for non-ideal fluid behavior.

The Peng-Robinson parameters are calculated from the critical properties and acentric factor of the selected compound.

The cubic equation in terms of the compressibility factor is then solved numerically to obtain the possible `Z` roots.

When three real roots are present:

The smallest root is treated as the liquid root
The largest root is treated as the vapor root

The fugacity coefficient is calculated from the selected `Z` root and Peng-Robinson parameters.

For vapor-liquid equilibrium, the program attempts to satisfy:
fL = fV
by iteratively adjusting the pressure.

## Compound Database

Thermodynamic properties are stored in the `Data_Table` dictionary.

Each compound currently contains:
[Tc, Pc, ω, Hv, Hf, Vl, Tv]

where:

Tc = critical temperature (K)
Pc = critical pressure (bar)
ω = acentric factor
Hv = enthalpy of vaporization (kJ/mol)
Hf = enthalpy of fusion (kJ/mol)
Vl = liquid molar volume (cm³/mol)
Tv = temperature associated with liquid molar volume data (K)

The database currently contains a range of gases, hydrocarbons, halogenated compounds, alcohols, aromatic compounds, and other common chemical species.

Additional compounds can be added directly to the dictionary.

## Program Workflow

Select Compound
       ↓
Retrieve Thermodynamic Properties
       ↓
Enter Temperature
       ↓
Calculate PR EOS Parameters
       ↓
Enter Initial Pressure Guess
       ↓
Solve Cubic EOS
       ↓
Calculate Z Roots
       ↓
Calculate Fugacity Coefficients
       ↓
Calculate Fugacity
       ↓
Equilibrium Calculation
       ↓
Iterate Pressure Until fL ≈ fV

The program can also calculate fugacity at a specified pressure without performing the equilibrium-pressure iteration.

## Example Output

A typical calculation reports:

--- Peng-Robinson Results ---
Final Pressure: XX.XXXXX bar
Liquid Fugacity Coefficient: X.XXXXXX
Vapor Fugacity Coefficient: X.XXXXXX
Liquid Fugacity: XX.XXXXX bar
Vapor Fugacity: XX.XXXXX bar
Liquid Z = X.XXXXXX
Vapor Z = X.XXXXXX

If only one real `Z` root is found, the program reports that an equilibrium pressure cannot be estimated from separate liquid and vapor roots.

## Requirements

Python 3.x
NumPy

## Running the Program

The program will prompt for:

1. Compound name
2. Temperature
3. Initial pressure guess
4. Whether to estimate equilibrium pressure

## Technologies

* Python
* NumPy
## Mathematical Methods
* Peng-Robinson Equation of State
* Numerical root solving
* Thermodynamic modeling

## Current Limitations

The current implementation is intentionally focused on a single-component Peng-Robinson calculation.

Current limitations include:

* Compound names must match the database entries
* The program currently uses a fixed property-table structure
* Only single-component calculations are supported
* Phase-root handling is based on the smallest and largest real roots
* Equilibrium calculations depend on an appropriate initial pressure and the presence of multiple real roots
* Additional validation and automated testing have not yet been implemented
