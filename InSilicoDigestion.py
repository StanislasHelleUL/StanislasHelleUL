# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:39:12 2022

@author: stan
"""
def writeRecord(sequences):

    try:
        if sequences[-1] !="\n":
            sequences = sequences + "\n"
    except:pass
        
    record={'ID':[],
            'Seq':[]
                }
    
    for n in range(len(sequences)):
        if sequences[n] == '>':
            thisID = ''
            for m in range(n+1,len(sequences)):
                if sequences[m] != '\n':
                    thisID += sequences[m]
                    
                else:
                    record['ID'].append(thisID)
                    thisSeq = ''
                    for o in range (m+1, len(sequences)):
                        if sequences[o] != '\n':
                            thisSeq += sequences[o]
                        else: 
                            try:
                                if sequences[o+1] == '>':
                                    thisSeq=thisSeq.strip()
                                    thisSeq=thisSeq.replace(' ', '')
                                    thisSeq=thisSeq.replace('\t', '')
                                    thisSeq=thisSeq.upper()
                                    record['Seq'].append(thisSeq)
                                    break
                                else:pass
                            except:
                                thisSeq=thisSeq.strip()
                                thisSeq=thisSeq.replace(' ', '')
                                thisSeq=thisSeq.replace('\t', '')
                                thisSeq=thisSeq.upper()
                                record['Seq'].append(thisSeq)
                    break
                
    if 'thisID' not in locals():
        thisID = 'userInput'
        record['ID'].append(thisID)
        sequences=sequences.strip()
        sequences=sequences.replace(' ','')
        sequences=sequences.replace('\t','')
        sequences=sequences.replace('\n','')
        sequences=sequences.upper()
        thisSeq = sequences
        record['Seq'].append(thisSeq)
            
    return record

def NoDigestion(sequences):
    record = writeRecord(sequences)
    finalPepList = [] 
    for protNb in range(len(record['Seq'])):
        IDPep = record['ID'][protNb]
        seqPep = record['Seq'][protNb]
        finalPepList.append((IDPep, seqPep))
    return tuple(finalPepList)
                   
def Trypsin(sequences):
    record = writeRecord(sequences)         
    finalPepList = []                           
    for protNb in range(len(record['Seq'])):
        IDPep = record['ID'][protNb]
        seqPep = record['Seq'][protNb]
        pepList = []
        n=0
        cutSites =[0]
        
        for n in range(len(seqPep)-1):
            if seqPep[n] == 'R' and seqPep[n+1] != 'P': 
                cutSites.append(n+1)
        
            elif seqPep[n] == 'K' and seqPep[n+1] != 'P':
                cutSites.append(n+1)
        
        if cutSites[-1] != len(seqPep):
            cutSites.append(len(seqPep))
            
        if len(cutSites) > 2:
            for cut in range(len(cutSites) -1): 
                pepDigN = seqPep[cutSites[cut]:cutSites[cut+1]]
                pepList.append(pepDigN)
        
        else: 
            pepList.append(seqPep)
        
        for peptide in pepList: 
            finalPepList.append((IDPep, peptide))
    
    return tuple(finalPepList)

def GingisKHAN_Kgp(sequences):
    record = writeRecord(sequences) 
    finalFragList = [] 
    for protNb in range(len(record['Seq'])):
        IDPep = record['ID'][protNb]
        seqPep = record['Seq'][protNb]
        fragList = []
        
        fragments = seqPep.split('KSCDKTHTCPPCP')

        if len(fragments)>1:
            fragment1 = fragments[0]+'KSCDK'
            fragList.append(fragment1)
            
            for x in range(1,len(fragments)-1):
    
                intermediate_fragment = 'THTCPPCP'+fragments[x]+'KSCDK'     
                fragList.append(intermediate_fragment)
                
            finalfragment = 'THTCPPCP'+fragments[-1]
            fragList.append(finalfragment)
        else:fragList = [seqPep]
                            
        for peptide in fragList: 
            finalFragList.append((IDPep, peptide))
                
    return tuple(finalFragList)
 
def FabULOUS_SpeB(sequences):
    record = writeRecord(sequences)         
    finalFragList = [] 
    for protNb in range(len(record['Seq'])):
        IDPep = record['ID'][protNb]
        seqPep = record['Seq'][protNb]
        fragList = []
        
        fragments = seqPep.split('KTHTCPPCPAPE')

        if len(fragments)>1:
            fragment1 = fragments[0]+'KTHT'
            fragList.append(fragment1)
            
            for x in range(1,len(fragments)-1):
    
                intermediate_fragment = 'CPPCPAPE'+fragments[x]+'KTHT'     
                fragList.append(intermediate_fragment)
                
            finalfragment = 'CPPCPAPE'+fragments[-1]
            fragList.append(finalfragment)
        else: fragList = [seqPep]
                            
        for peptide in fragList: 
            finalFragList.append((IDPep, peptide))
                
    return tuple(finalFragList)
    
def FabRICATOR_IdeS(sequences):
    record = writeRecord(sequences)         
    finalFragList = [] 
    for protNb in range(len(record['Seq'])):
        IDPep = record['ID'][protNb]
        seqPep = record['Seq'][protNb]
        fragList = []
        
        if "LGGPSVFLF" in seqPep:
            fragments = seqPep.split('LGGPSVFLF')

            if len(fragments)>1:
                fragment1 = fragments[0]+'LG'
                fragList.append(fragment1)
                
                for x in range(1,len(fragments)-1):
        
                    intermediate_fragment = 'GPSVFLF'+fragments[x]+'LG'     
                    fragList.append(intermediate_fragment)
                    
                finalfragment = 'GPSVFLF'+fragments[-1]
                fragList.append(finalfragment)
        
        elif "VAGGPSVFLF" in seqPep:
            fragments = seqPep.split('VAGPSVFLF')

            if len(fragments)>1:
                fragment1 = fragments[0]+'LG'
                fragList.append(fragment1)
                
                for x in range(1,len(fragments)-1):
        
                    intermediate_fragment = 'GPSVFLF'+fragments[x]+'VA'     
                    fragList.append(intermediate_fragment)
                    
                finalfragment = 'GPSVFLF'+fragments[-1]
                fragList.append(finalfragment)
            
        else: fragList = [seqPep]
                             
        for peptide in fragList: 
            finalFragList.append((IDPep, peptide))
                
    return tuple(finalFragList)