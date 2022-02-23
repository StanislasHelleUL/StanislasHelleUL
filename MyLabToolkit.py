# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:54:38 2022

@author: Stanislas.Helle

this module allows to calculate the mass you need to weight for each 
solid components composing your buffer. It uses PUGREST API from PubChem
to retrieve the molecular weight (MW) of components by simply indicating 
their names, you don't have to look after the MW yourself anymore!
I Hope you will find this module usefull!
"""

from urllib.request import urlopen as url

class CalcMasses():
    def findMW(name):
        path = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/MolecularWeight/TXT' 
        with url(path) as request:
            response = request.read().decode('utf-8')
            try:
                response = float(response)
            
            #if several MW exist for a component (i.e. amino-acids in their acidic, zwitterion and alkaline form)
            # response will be a string of this form: 'a\nb\nc\n'... which cannot be converted as a float
            # the exception will convert response in a list and the user will have to choose one value
            except: 
                response = response.split('\n')
                response.remove('')
    
                # if several items in the list have the same value, creating a set will remove the iterations
                response = set(response)
                response = list(response)
                
                if len(response) >2:
                    print('several MW values were proposed for your component, please choose the one which seems correct to you:')
                    for index, mw in enumerate(response):
                        print(f'{index}:\t{mw}')
                        
                    in_range = False
                    while in_range == False:
                        chosen_index = input('Indicate here the index of the MW you have chosen: ')
                        try:
                            chosen_index = int(chosen_index)
                            if chosen_index in range(len(response)):
                                in_range = True
                            else:
                                print('the index you indicated is out for range, please indicate a valid index.')
                        except:
                            print('your input is not an integer, please indicate the index, not the MW.')
                            
                    response = float(response[chosen_index])
                
                #if there is only one value in the list, there is no need to ask the user for choosing an index
                else:
                    response = float(response[0])
        print(f'MW of {name}:\t{response}')
        return response
    
    is_int = False    
    while is_int == False:
        compNum = input('How many solid components do you have in your buffer?: ')
        try:
            compNum = int(compNum)
            is_int = True
        except: print('Please, give an integer as value')
    
    is_num = False
    while is_num == False:
        finalV = input('What is the final volume of your buffer? (in mL): ')
        try: 
            finalV = float(finalV)
            is_num = True
        except: print('Please, give a number as value') 
    
    compDict = {
        'Name':[],
        'MW': [],
        'Concentration':[]
        }
    
    for x in range(1,compNum+1):
        validName = False
        while validName == False:
            compName = input(f'Name of component {x}: ')  
            try:
                compMW = findMW(compName)
                validName = True
            except: print("can't find your component in PubChem, verify if there is no typo.\nIf the name of your component is composed of several words, use '-' instead of a space")
        compDict['Name'].append(compName)
        compDict['MW'].append(compMW)
    
        is_num = False
        while is_num == False:    
            compC = input(f'Concentration of component {x} (in mM): ')
            try:
                compC = float(compC)
                is_num = True
            except: print('Please, give a number as value')        
        compDict['Concentration'].append(compC)
    
    print('You will need:')
    for x in range(len(compDict['Name'])):
        name = compDict['Name'][x]
        M = float(compDict['MW'][x])
        C = float(compDict['Concentration'][x])
        
        mass = C*M*finalV*0.001
    
        print(f'{round(mass, 1)} mg of {name}')