# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:16:30 2022

@author: Stanislas.Helle
"""

from DictioProt import aminoDict, modDict, atomDict, adductPosDict
import scipy.special as sps

def peptideMW(sequence):
    
    pepmass = 0.0
    if sequence == '':
        pass
    else:
        for aa in sequence:
            
            indexAa = aminoDict['Code'].index(f'{aa}')
            aamass = aminoDict['Mono'][indexAa]
            pepmass += aamass
        
        pepmass += 18.01528
    return(round(pepmass,3))

def mzPeakMassif(accession = "userInput", sequence= "", charge = 1,
                 adduct = "Proton", modification = "None"):
    monoIsotopicMass = peptideMW(sequence)
    if modification != "None":
        modIndex = modDict['Name'].index(modification)
        residues = modDict['Residue'][modIndex]
        counter = 0
        for char in residues:
            counter += sequence.count(char)
        monoIsotopicMass += modDict['Mono'][modIndex] * counter
    indexAdduct = adductPosDict['Name'].index(f'{adduct}')
    adductMass = adductPosDict['Mass'][indexAdduct]
    PepCarbonNb = 0
    
    for aa in sequence:
        indexAa = aminoDict['Code'].index(f'{aa}')
        aaComposition = aminoDict['Comp'][indexAa]
        
        for n in range(len(aaComposition)): 
            if aaComposition[n] == 'C':
                str_carbon_number = ''
                for m in range(n+1, len(aaComposition)):
                    try:
                        int(aaComposition[m])
                        str_carbon_number += aaComposition[m]
                    except:
                        break
                if str_carbon_number == '':
                    PepCarbonNb += 1
                else:
                    PepCarbonNb += int(str_carbon_number)
             
    c12_proba = atomDict['Mono_Abn'][1]
    c13_mass_difference = 1.0034
    
    #create a list with the percentage value of each isotope
    isotopeProbaList = []
    for x in range(PepCarbonNb):
        percent_isotope = sps.binom(PepCarbonNb, x)*(1-c12_proba)**(x)*(c12_proba)**(PepCarbonNb-x)
        isotopeProbaList.append(percent_isotope)

    #create a reduced list with values that are actually significant: 
    #higher than 1 ppm compared to the highest value.
    highest_value = max(isotopeProbaList)
    reduced_list = [x for x in isotopeProbaList if x > highest_value/1000000]
    
    peakMassif = []
    for i in range(len(reduced_list)-1):

        mz = (float(monoIsotopicMass) + (c13_mass_difference * i))/charge + adductMass
        relative_Abn = reduced_list[i]
        peakMassif.append((mz, relative_Abn))
          
    return tuple(peakMassif)