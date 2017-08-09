#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:13:45 2017
Author - Ben Nicholl
"""
#  below is a youtube video explaining minmax algorithm 
#  https://www.youtube.com/watch?v=zDskcx8FStA
 
import numpy as np
import copy

np.set_printoptions(threshold=np.inf)

"""pre made board, although this algo can work with any numpy array""" 
c_four = np.array([
                  [0,0,0,0,0,0,0,0],  
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0]    
                  ])

""" to run this algo, simply call the class, and type the c_four numpy board in the argument I hashtaged an example of how to do so below"""
#  play = connect(c_four)  

class connect():
    
    def __init__(self, connect_four):
        self.connect_four = connect_four
        self.possible_states()    

    def possible_states(self):
        
        self.array = copy.deepcopy(self.connect_four)
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
                #print('d_1','1',e)
                #print(self.states[fifth_d][fourth_d][0])
                
                
                """iterates through all elements in the second to last row"""
                """this level of if statements calculates state of 4th dimension"""
                if i[-2] == 0:       
                    """new 4th dimension"""
                    third_d = 0
                    #  we now have created a self.states[0][1][0]
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-2][e] = 2
                    #print('d_2','2',e)
                    #print(self.states[fifth_d][fourth_d][0])
                    
                    
                    """iterates through all elements in the third to last row"""
                    """this level of if statements calcualtes state of terminal nodes(3rd dimension)"""                      
                    if i[-3] == 0:
                        #  we now have created a self.states[0][1][1]
                        #  we always want the last index to be zero, like in the line below so it goes back to the original state
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-3][e] = 2
                        #print('d_3','3',e) 
                        #print(self.states[fifth_d][fourth_d][third_d])
                        
                    
                    """these check if columns directly left and right on the -2 row == 0 and if the rows beneath them != 0"""   
                    if e+1 < self.array.shape[1] and self.array[-2][e+1] == 0 and self.array[-1][e+1] != 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e+1] = 2
                        #print('d_3','4',e)
                        #print(self.states[fifth_d][fourth_d][third_d])
                                        
                    if e-1 >= 0 and self.array[-2][e-1] == 0 and self.array[-1][e-1] != 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e-1] = 2 
                        #print('d_3','5',e)
                        #print(self.states[fifth_d][fourth_d][third_d])
                        
     
                """1st and 2nd if statement check if 2x depth directly right columns on the -1 row == 0"""    
                if e+1 < self.array.shape[1] and self.array[-1][e+1] == 0:
                    third_d = 0
                    """new 4th dimension"""
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-1][e+1] = 2
                    #print('d_2','6',e)
                    #print(self.states[fifth_d][fourth_d][0])
                    
                    
                    if e+2 < self.array.shape[1] and self.array[-1][e+2] == 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-1][e+2] = 2  
                        #print(self.states[fifth_d][fourth_d][third_d])   
                        #print('d_3','7',e)
                        
                    """checks if one right, one up == 0"""    
                    if self.array[-2][e+1] == 0:  
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e+1] = 2
                        #print('d_3','8',e)
                        #print(self.states[fifth_d][fourth_d][third_d])
                        
                    
                """1st and 2nd if statement check if 2x depth directly left columns on the -1 row == 0""" 
                if e - 1 >= 0 and self.array[-1][e-1] == 0:
                    third_d = 0
                    self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                    fourth_d += 1
                    self.states[fifth_d][fourth_d][0][-1][e-1] = 2
                    #print('d_2','9',e)
                    #print(self.states[fifth_d][fourth_d][0])
                                  
                    if e - 2 >= 0 and self.array[-1][e-2] == 0:  
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-1][e-2] = 2
                        #print('d_3','10',e)
                        #print(self.states[fifth_d][fourth_d][third_d])
                        
                    """checks if one left, one up == 0"""    
                    if self.array[-2][e-1] == 0:
                        self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                        third_d +=1
                        self.states[fifth_d][fourth_d][third_d][-2][e-1] = 2
                        #print('d_3','11',e) 
                        #print(self.states[fifth_d][fourth_d][third_d])
                           
                        
        """this while/for loop checks all elements whose -1st row are != 0"""     
        while index_value > -self.array.shape[0]: #  use .shape on this 
            """index value decreses by one every loop, thus iterating through each row"""
            index_value -= 1            
            for e,i in enumerate(self.array.T):                
                fourth_d = 0
                """iterates through all elements of -2 row where -1 row are != 0"""
                if abs(index_value - 1) <= self.array.shape[0] and i[index_value] != 0 and i[index_value-1] == 0:
                    fifth_d += 1
                    """new 5th dimension created"""
                    self.states.append(copy.deepcopy([[self.array]]))
                    self.states[fifth_d][fourth_d][0][index_value - 1][e] = 2 
                    #print('d_1','12',e)
                    #print(self.states[fifth_d][fourth_d][0])
                    
                    
                    if abs(index_value - 2) <= self.array.shape[0] and i[index_value-2] == 0:
                        """new 4th dimension"""
                        third_d = 0
                        #  we now have created a self.states[0][1][0]. for first iteration, that is
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-2][e] = 2
                        #print('d_2','13',e)
                        #print(self.states[fifth_d][fourth_d][0])
                        
                        
                        if abs(index_value - 3) <= self.array.shape[0] and i[index_value-3] == 0:                   
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-3][e] = 2
                            #print('d_3','14',e) 
                            #print(self.states[fifth_d][fourth_d][third_d])
                            
                            
                        """check is index value - 2 and e +/- 1 == 0, while index value -1 and e +/- 1 != 0 """       
                        if e+1 < self.array.shape[1] and self.array[index_value-2][e+1] == 0 and self.array[index_value-1][e+1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e+1] = 2
                            #print('d_3','15',e) 
                            #print(self.states[fifth_d][fourth_d][third_d])
                                           
                        if e - 1 >= 0 and self.array[index_value-2][e-1] == 0 and self.array[index_value-1][e-1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e-1] = 2
                            #print('16',e)
                            #print('d_3',self.states[fifth_d][fourth_d][third_d])
                            
                    """checks if the e+1 value is == 0"""
                    if e+1 < self.array.shape[1] and self.array[index_value-1][e+1] == 0 and self.array[index_value][e+1] != 0:
                        third_d = 0
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-1][e+1] = 2
                        #print('17',e)  
                        #print('d_2',self.states[fifth_d][fourth_d][0])
                        
                        """checks if the e+1 value and the row above the iterator is == 0"""
                        
                        if abs(index_value - 2) <= self.array.shape[0] and self.array[index_value-2][e+1] == 0:# and self.array[index_value-1][e+1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e+1] = 2
                            #print('d_3','18',e)
                            #print(self.states[fifth_d][fourth_d][third_d])
                            
                            """checks if the e+2 value is == 0"""
                        if e+2 < self.array.shape[1] and self.array[index_value-1][e+2] == 0 and self.array[index_value][e+2] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-1][e+2] = 2
                            #print('d_3','19',e)
                            #print(self.states[fifth_d][fourth_d][third_d])
                            
                    """checks if the e-1 value is == 0"""        
                    if e - 1 >= 0 and self.array[index_value-1][e-1] == 0 and self.array[index_value][e-1] != 0:
                        third_d = 0
                        self.states[fifth_d].append(copy.deepcopy(self.states[fifth_d][0]))
                        fourth_d += 1
                        self.states[fifth_d][fourth_d][0][index_value-1][e-1] = 2
                        #print('d_2','20',e)
                        #print(self.states[fifth_d][fourth_d][0])
                        
                        """checks if the e-1 value and the row above the iterator is == 0"""
                        if abs(index_value - 2) <= self.array.shape[0] and self.array[index_value-2][e-1] == 0:# and self.array[index_value-1][e-1] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-2][e-1] = 2
                            #print('d_3','21',e)
                            #print(self.states[fifth_d][fourth_d][third_d])
                            
                        """checks if the e-2 value is == 0"""
                        if e - 2 >= 0 and self.array[index_value-1][e-2] == 0 and self.array[index_value][e-2] != 0:
                            self.states[fifth_d][fourth_d].append(copy.deepcopy(self.states[fifth_d][fourth_d][0]))
                            third_d += 1
                            self.states[fifth_d][fourth_d][third_d][index_value-1][e-2] = 2
                            #print('d_3','22',e)
                            #print(self.states[fifth_d][fourth_d][third_d])
                            
        self.h_value()
                        
    def h_value(self):
        
        self.h_values = []
        """represents the 5th index"""
        fifth_d = -1
        
        """ this while loop iterates through all of the initial states. ie the 5th element"""
        while fifth_d < len(self.states) - 1: # -1 instead of 0 because the first time it runs through this loop it is -1

            fifth_d += 1
                         
            """this checks is there is multiple states in the 4th index. AKA, it checks if there is another option after the intial move"""
            if len(self.states[fifth_d]) > 1: 
                fourth_d = 0
                
                """elif there is not more than one option after initial move AKA a depth of one"""    
            elif len(self.states[fifth_d]) == 1:
                fourth_d = -1
                                  
            """ensure the fourth_d variable is less than the total number of possible paths, or indexes in the fourth dimension"""
            #  for example, if the max fourth dimension index in the 1st fifth dimension is 4 ( [1][4] ), this loop will check [1][1] through [1][4]
            while fourth_d < len(self.states[fifth_d]) - 1:
                
                fourth_d += 1
                terminal_index = 0
                """gives a value of 2 if there is one 1 depth states and 3 if there are two 2 depth states"""
                terminal_indices = len(self.states[fifth_d][fourth_d])
                """if the terminal_indices == 1, there is a depth of two, and thus only one iteration, so treat it as such"""
                if terminal_indices == 1:
                    terminal_indices += 1
                """if terminal indices == 3, their are two iterations which are the -1th and -2th state"""
                """if terminal indices == 2, their is one iteration which is the -1th state"""
                # this is where each -i'th row starts, thus a new terminal state h score is zero'd 
                while terminal_indices > 1:                        

                    terminal_indices -= 1                    
                    terminal_index -= 1
                    terminal_state_score = 0
                    row = -2
                    
                    """when the row level has reached the final row, its gets brough back to this while loop, and the h_value and indexes get appended to h_values list"""
                    while row < c_four.shape[1]:
                        # if this while loop is read, and it is greater than the intial instantiation of -2, than that specific terminal state has completed its iterations
                        """if this below if statement is true, add one to row so it wont be true next loop, and append the h_values and indexes acordingly"""
                        if row > -2:
                            row += 1
                            self.h_values.append([fifth_d,fourth_d,terminal_index,len(self.states[fifth_d][fourth_d]),terminal_state_score])
                            #  I should prune states with a -1 and -2 path here
                            #  on second thought, I will just prune everything under ABprune method
                            
                        """both of these while loops iterate through all of the individual elements within the arrays and assign values to each state based off of the amount of 2's there are in a row/column"""
                        while row < c_four.shape[1] - 1:
                            row += 1
                            column = 0
                                                       
                            while abs(column) < c_four.shape[0]:
                                column -= 1                                
          
                                #print('fifth',fifth_d)
                                #print('fourth',fourth_d)
                                #print('ter',terminal_index)
                                #print('column',column)
                                #print('row',row) 
                                
                                """the below if and elif statements begin assigning values to states"""                                
                                    
                                """checks down to up on each column, the amount of 2's that are next to eachother"""                                
                                if abs(column) <= c_four.shape[0] - 3:
                                    #  two
                                    if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 1][row] == 2:     
                                        terminal_state_score += 2                                       
                                        #  three    
                                        if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 1][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 2][row] == 2:    
                                            terminal_state_score += 6   
                                            #four
                                            if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 1][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 2][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column - 3][row] == 2:
                                                terminal_state_score += 20
                                 
                                """checks right to left on each row, the amount of 2's that are next to eachother"""    
                                if row + 3 < c_four.shape[1]:
                                    #  two    
                                    if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 1] == 2:              
                                        terminal_state_score += 2
                                         #  three    
                                        if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 2] == 2:
                                            terminal_state_score += 5
                                            #  four                                                                                                                   
                                            if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 2] == 2 and self.states[fifth_d][fourth_d][terminal_index][column][row + 3] == 2:
                                                terminal_state_score += 20
                                    
                                """checks diagnolly bottom to the top from the left to RIGHT direction, the amount of 2's that are next to each other"""
                                if abs(column) <= c_four.shape[0] - 3 and row + 3 < c_four.shape[1]:
                                    # two
                                    if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row + 1] == 2:
                                        terminal_state_score += 2     
                                        # three
                                        if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row + 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 2][row + 2] == 2:
                                            terminal_state_score += 5
                                            # four
                                            if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row + 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 2][row + 2] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 3][row + 3] == 2:
                                                terminal_state_score += 20
                                    
                                """checks diagnolly bottom to the top from the right to LEFT direction, the amount of 2's that are next to each other"""
                                
                                if abs(column) <= c_four.shape[0] - 3 and row >= 3:    
                                    # two                                                           
                                    if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row - 1] == 2:
                                        terminal_state_score += 2
                                        # three
                                        if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row - 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 2][row - 2] == 2:
                                            terminal_state_score += 5
                                            # four
                                            if self.states[fifth_d][fourth_d][terminal_index][column][row] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 1][row - 1] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 2][row - 2] == 2 and self.states[fifth_d][fourth_d][terminal_index][column + 3][row - 3] == 2:
                                                terminal_state_score += 20
                                
        print(self.h_values)                            
        self.maximum()
    def maximum(self):
        
        for e,i in enumerate(self.h_values):           
            
        
            beta = 1000
            
            """checks for the paths with one 3 depth state"""
            if i[3] == 2:
                
                """the reason we pop if the i[4] > beta is because the next depth will take the min value"""               
                if i[4] < beta:
                    beta = i[4]
                    """this puts the third_d index in its new path state, which is now the second depth"""
                    self.h_values[e][2] = 0
                    """else i[4] >= beta"""
                else: 
                    self.h_values.pop(e)
                    
                    """elif the iterator has two 3 depth states and it is the -1'th state"""
                    """I only want the -1'th state because I check both via enumerator +1 in the below if statements"""
            elif i[3] == 3 and i[2] == -1:
                
                """this if statements prunes the remaining state if the alpha is exceeded by the -1'th state"""
                """if the -1'th state in the two 3 depth state (AKA the first state I check) is greater than beta, pop the -1'th and -2'th state"""
                if i[4] > beta:                    
                    self.h_values.pop(e)
                    if e+1 < len(self.h_values):
                        self.h_values.pop(e+1)
                
                elif i[4] < beta:               
                    """take the max of the 3rd depth"""                    
                    if self.h_values[e][4] >= self.h_values[e+1][4]:
                        # i use the h_values array instead of the i iterator just to keep it congruent with the rest of this specific if statement
                        beta = self.h_values[e][4]
                        self.h_values[e][2] = 0
                        if e+1 < len(self.h_values):
                            self.h_values.pop(e+1)
                        
                    elif e+1 < len(self.h_values) and self.h_values[e][4] < self.h_values[e+1][4]:
                        beta = self.h_values[e+1][4]
                        self.h_values[e+1][2] = 0
                        self.h_values.pop(e)
        self.minimum()
                        
    def minimum(self):
        self.alpha = 0
        list_index = 0
            
        while list_index < len(self.h_values):
            #print('1',list_index)
            """this ensures that states with a depth of one are not iterated through"""
            if self.h_values[list_index][1] != 0:

                """no matter which iteration it is in within that given index, if a value of < alpha is given, prune all of those values"""
                # I may want to make this a <= rather than <
                if self.h_values[list_index][4] < self.alpha:
                    """this variable is used to refind the proper index in the below if/while loop"""
                    fifth_index_before_prune = self.h_values[list_index][0]
                    """list comprehension in order prune all of the the lists within the list that have a fifth_dimension value == to what is being indexed via fifth_index"""
                    self.h_values = [i for i in self.h_values if i[0] != self.h_values[list_index][0]]                            
                    """checks if the newly pruned list is indexing a value that doesnt exist due to pruning"""
                    if list_index < len(self.h_values):
                        """iterate back through list until fifth_index is indexing an integer that is < the previusly pruned fifth_index integer"""
                        while self.h_values[list_index][0] > fifth_index_before_prune:
                            list_index -= 1
                        list_index += 1  
                        
                        """if the newly pruned h_vaues is indexing an index that doesnt exist, reset it so it indexes the last list within the lists, than interates til it reaches a fifth_index value less than the prunded indexes"""    
                    else:
                        list_index = len(self.h_values) - 1 
                        while self.h_values[list_index][0] > fifth_index_before_prune:
                            list_index -= 1
                        list_index += 1    
     
    
                    """if the fifth index value and fifth index value + 1 are the same"""
                elif list_index + 1 < len(self.h_values) and self.h_values[list_index][0] == self.h_values[list_index+1][0]:
                    
                    """find the minimum of the states in the same fifth dimension"""
                    if self.h_values[list_index][4] >= self.h_values[list_index+1][4]:
                        #  when I pop this, I dont add the fifth index because it will now be reading the list below the poped list, since that list has been removed
                        self.h_values.pop(list_index)
                        self.alpha = self.h_values[list_index][4]  
                    elif self.h_values[list_index][4] < self.h_values[list_index+1][4]:
                        self.h_values.pop(list_index + 1)
                        # again, the fifth_index does not have a + 1 added to it becuase it takes the same index when the we pop the previous fifth_index
                        self.alpha = self.h_values[list_index][4]
                        
                elif list_index + 1 < len(self.h_values) and self.h_values[list_index][0] != self.h_values[list_index+1][0]:
                    if list_index < len(self.h_values):
                        list_index += 1
                    """if the last h_value does not meet the criteria of the if statement in this block of if/elif's, run this else statement"""
                else:
                    list_index += 1
                """if the state does have a depth of one"""            
            else:
                list_index += 1
                
        self.computer_choose_state()        
    def computer_choose_state(self):
        greatest_number = 0
        for i in self.h_values:
            """if the hueristic is greater than the current highest value, save the fifth index dimension under fifth dimension"""
            if i[4] > greatest_number:
                greatest_number = i[4]
                fifth_dimension = i[0]
                print(greatest_number)
        """this saves the first possible state, in the 3 depth path"""        
        self.connect_four = self.states[fifth_dimension][0][0]
        
        print(self.connect_four)
        self.player_choose_position()
        
        """this method allows the player playing against the AI to choose his or hers position"""
    def player_choose_position(self):
        
        column = int(input('type your desired column, with the most bottom column starting at 1: '))
        if column > c_four.shape[0] or column <= 0:
            print('answer is invalid, try again')
            self.player_choose_position()
                       
        row = int(input('type your desired row, with the most left row starting at 1: ')) 
        if row > c_four.shape[1] or row <= 0:
            print('answer is invalid, try again')
            self.player_choose_position() 
        #print('yyeeaa')    
        if self.connect_four[-column][row-1] != 0:
            print('answer is invalid, try again')
            self.player_choose_position()
        else:                      
            self.connect_four[-column][row-1] = 1
        
        self.possible_states()
        
                            

        
            
            
            
    
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            