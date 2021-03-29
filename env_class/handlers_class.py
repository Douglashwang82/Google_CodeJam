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
    
    def type1_output(self,results):
        """ For output structure like:
            Case #(number): (results)
            Tale results(list)
        """
        
        for i in range(len(results)):
            print("Case {}: {}".format(i, results[i]))
        
