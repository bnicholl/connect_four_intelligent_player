#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:13:45 2017

@author: bennicholl
"""
import numpy as np
import copy

np.set_printoptions(threshold=np.inf)

c_four = np.array([
                  [0,0,0,0,0,0],  
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,1],
                  [1,0,0,0,0,1],
                  [1,0,0,0,0,1],
                  [1,0,1,1,1,2]    
                  ])

class connect():
    
    def __init__(self):
    
        self.moves()    

  #  I can either create deepcopies or save the indexes 
  #  and run them through the array, than claculate scores. 

    def moves(self):
        
        self.array = copy.deepcopy(c_four)
        self.states = []
        """iterates the index values in the while loop"""
        index_value = 0
        """as it iterates through the first if statement += 1 is added increase # of 5th dimensions""" 
        fifth_d = -1
        
        #  I need to save every single possible state in a deepcopy
        #  save the state with the enumerator number
        #  and when you call each enumerator number, index it from the -1
        for e,i in enumerate(self.array.T):
            """iterates through all elements in the -1st row"""
            """this level of if statements calcualtes state of 5th dimension"""
            
            """fourth_d will be zerod everytime a new 5th dimension"""
            fourth_d = 0
            
            if i[-1] == 0:
                fifth_d += 1
                #  adds a copy of self.array, than calls the += list_value
                #  to that third dimensional array
                """new 5th dimension created"""
                #  we now have created a self.states[0][0][0]
                self.states.append(copy.deepcopy([[self.array]]))               
                self.states[fifth_d][fourth_d][0][-1][e] = 2
                print(self.states[fifth_d][fourth_d][0])
                print('1',e)
                
                """iterates through all elements in the second to last row"""
                """this level of if statements calculates state of 4th dimension"""
                if i[-2] == 0:       
                    """new 4th dimension"""
                    third_d = 0
                    #  we now have created a self.states[0][1][0]
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-2][e] = 2
                    print(self.states[fifth_d][fourth_d][0])
                    print('2',e)
                    
                    """iterates through all elements in the third to last row"""
                    """this level of if statements calcualtes state of terminal nodes(3rd dimension)"""                      
                    if i[-3] == 0:
                        #  we now have created a self.states[0][1][1]
                        #  we always want the last index to be zero, like in the line below so it goes back to the original state
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-3][e] = 2
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('3',e) 
                    
                    """these check if columns directly left and right on the -2 row == 0 and if the rows beneath them != 0"""   
                    if e+1 < self.array.shape[1] and self.array[-2][e+1] == 0 and self.array[-1][e+1] != 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e+1] = 2
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('4',e)                
                    if e-1 >= 0 and self.array[-2][e-1] == 0 and self.array[-1][e-1] != 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e-1] = 2 
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('5',e)
     
                """1st and 2nd if statement check if 2x depth directly right columns on the -1 row == 0"""    
                if e+1 < self.array.shape[1] and self.array[-1][e+1] == 0:
                    third_d = 0
                    """new 4th dimension"""
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-1][e+1] = 2
                    print(self.states[fifth_d][fourth_d][0])
                    print('6',e)
                    
                    if e+2 < self.array.shape[1] and self.array[-1][e+2] == 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-1][e+2] = 2  
                        print(self.states[fifth_d][fourth_d][third_d])                        
                        print('7',e)
                    """checks if one right, one up == 0"""    
                    if self.array[-2][e+1] == 0:  
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e+1] = 2
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('8',e)
                    
                """1st and 2nd if statement check if 2x depth directly left columns on the -1 row == 0""" 
                if e - 1 >= 0 and self.array[-1][e-1] == 0:
                    third_d = 0
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-1][e-1] = 2
                    print(self.states[fifth_d][fourth_d][0])
                    print('9',e)              
                    if e - 2 >= 0 and self.array[-1][e-2] == 0:  
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-1][e-2] = 2
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('10',e)
                    """checks if one left, one up == 0"""    
                    if self.array[-2][e-1] == 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e-1] = 2
                        print(self.states[fifth_d][fourth_d][third_d])
                        print('11',e)    
                        
        """this while/for loop checks all elements whose -1st row are != 0"""     
        while index_value > -self.array.shape[0]: #  use .shape on this 
            """index value decreses by one every loop, thus iterating through each row"""
            index_value -= 1            
            for e,i in enumerate(self.array.T):                
                fourth_d = 0
                """iterates through all elements of -2 row where -1 row are != 0"""
                if i[index_value] != 0 and i[index_value-1] == 0:
                    fifth_d += 1
                    """new 5th dimension created"""
                    self.states.append(copy.deepcopy([[self.array]]))
                    self.states[fifth_d][fourth_d][0][index_value - 1][e] = 2 
                    print(self.states[fifth_d][fourth_d][0])
                    print('12',e)
                    
                    if abs(index_value - 2) <= self.array.shape[0] and i[index_value-2] == 0:
                        """new 4th dimension"""
                        third_d = 0
                        #  we now have created a self.states[0][1][0]. for first iteration, that is
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-2][e] = 2
                        print(self.states[fifth_d][fourth_d][0])
                        print('13',e)
                        
                        if abs(index_value - 3) <= self.array.shape[0] and i[index_value-3] == 0:                   
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-3][e] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('14',e) 
                            
                        """check is index value - 2 and e +/- 1 == 0, while index value -1 and e +/- 1 != 0 """       
                        if e+1 < self.array.shape[1] and self.array[index_value-2][e+1] == 0 and self.array[index_value-1][e+1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-1][e+1] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('15',e)                
                        if e - 1 >= 0 and self.array[index_value-2][e-1] == 0 and self.array[index_value-1][e-1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e-1] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('16',e)
                    """checks if the e+1 value is == 0"""
                    if e+1 < self.array.shape[1] and self.array[index_value-1][e+1] == 0 and self.array[index_value][e+1] != 0:
                        third_d = 0
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-1][e+1] = 2
                        print(self.states[fifth_d][fourth_d][0])
                        print('17',e)  
                        """checks if the e+1 value and the row above the iterator is == 0"""
                        if self.array[index_value-2][e+1] == 0:# and self.array[index_value-1][e+1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e+1] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('18',e)
                            """checks if the e+2 value is == 0"""
                        if e+2 < self.array.shape[1] and self.array[index_value-1][e+2] == 0 and self.array[index_value][e+2] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-1][e+2] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('19',e)
                    """checks if the e-1 value is == 0"""        
                    if e - 1 >= 0 and self.array[index_value-1][e-1] == 0 and self.array[index_value][e-1] != 0:
                        third_d = 0
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-1][e-1] = 2
                        print(self.states[fifth_d][fourth_d][0])
                        print('20',e)
                        """checks if the e-1 value and the row above the iterator is == 0"""
                        if self.array[index_value-2][e-1] == 0:# and self.array[index_value-1][e-1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e-1] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('21',e)
                        """checks if the e-2 value is == 0"""
                        if e - 2 >= 0 and self.array[index_value-1][e-2] == 0 and self.array[index_value][e-2] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-1][e-2] = 2
                            print(self.states[fifth_d][fourth_d][third_d])
                            print('22',e)
                            
        
        
                
        
        
        
        
        
        
        
    