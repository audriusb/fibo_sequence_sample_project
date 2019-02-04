"""
Sequence generators
"""

class Fibonacci_Sequence:
    """
    Fibonacci sequence generator class
    """
    @classmethod
    def __nth_fibonacci(cls, n):
        """
        Fetches the nth fibonacci sequence number
        """
        a = 0
        b = 1
        if n == 0: 
            return a 
        elif n == 1: 
            return b 
        else: 
            for _ in range(2, n+1): 
                c = a + b 
                a = b 
                b = c 
            return b
    
    @classmethod
    def generate_fibonnaci_seq(cls, start, end): 
        """
        Generates fibonacci sequence array from provided start and end values
        """
        sequence = []
        if start < 0:
            raise IndexError
        elif start > end:
            raise IndexError
        elif end > 100000:
            raise IndexError
        elif end == 0: #if you need nothing, we'll give you nothing
            return {'length': 0, 'sequence': []}
        elif end == 1: #only first number. okay.
            return {'length': 0, 'sequence': [0]}
        
        
        if start > 0: #if start is not from 0, lets fetch the first 2 members
            sequence.append(Fibonacci_Sequence.__nth_fibonacci(start))
            sequence.append(Fibonacci_Sequence.__nth_fibonacci(start+1))
        else: #else, we know the first two members
            sequence.append(0)
            sequence.append(1)

        if end - start > 2: #sequence length is more than alredy calculated
            for _ in range(start+2, end):
                sequence.append(sequence[-1] + sequence[-2])

        result = {
            'length': end - start,
            'sequence': sequence
            }
        return result
