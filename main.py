"""
Take Input ( from Sample.txt )
Show Output
"""

class InputHandler:
    """ Handle general INPUT requirement"""

    def __init__(self):
        """ Initial the Handler object.
        Usually takes the first element as number of cases to be tested.
        Second argument is used to define 
        """
        self._amountOfCases = ""
        self._samples = []
    
    def set_amount_cases(self):
        """Setting the amount of cases"""
        user_input = input()
        self._amountOfCases = user_input
    
    def type_1_input(self):
        """ Handle input structure like:
        cases
        sample_1_intro (One integer)
        sample_1_data (data seperate by blank)
        sample_2_intro
        sample_2_data
        """
        for _ in range(int(self._amountOfCases)):
            user_input_intro = input() # may not being use in python
            user_input_data = input()
            split_the_string = user_input_data.split(" ")
            self._samples.append(split_the_string)
    
    def type_2_input(self):
        """ Handle input structure like:
            cases
            sample_1
            sample_2
        """
        for _ in range(int(self._amountOfCases)):
            user_input = input()
            split_the_string = user_input.split(" ")
            self._samples.append(split_the_string)
    
    def get_samples(self):
        """ Return the samples set."""
        return self._samples


class OutputHandler():
    """ Handle general OUTPUT requirements"""

    def __init__(self):
        """Results is a list"""
        self._result = []
    
    def set_result(self, result):
        """ Handle Result"""
        self._result = result

    def get_result(self):
        """return result"""
        return self._result

    def type1_output(self):
        """ For output structure like:
            Case #(number): (results)
            Tale results(list)
        """
        
        for i in range(len(self._result)):
            print("Case {}: {}".format(i + 1, self._result[i]))
        



""" Main program to run the test code

"""

# libraries
# from env_class import handlers_class  save for online submitting
from CodeJam2021.Round_1A.p2.solution import Solution

# data sectin
ih = InputHandler()
oh = OutputHandler()
solution = Solution()

# input
ih.set_amount_cases() # get the amount of cases from user
ih.type_2_input()

# logic section



# output
oh.type1_output()



