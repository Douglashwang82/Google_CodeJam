class Solution:
    """ Logic for the program. It may contain several functions."""
        
    def Reversort(self, L):
        #For anser
        sum = 0

        for i in range(len(L) - 1):
            j = L.index(min(L[i:]))

            # Reverse(L[i:j])
            front = L[:i]
            middle = L[i:j+1]
            back = L[j+1:]
            middle.reverse()
            L = front + middle + back
            sum += len(middle)

        return sum
    

    def Solve(self, samples):
        """Handle the samples"""
        output = []
        for s in samples:
            output.append(self.Reversort(s))
        return output
        