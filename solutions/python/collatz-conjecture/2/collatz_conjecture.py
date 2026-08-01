"""
collatz conjecture program. it is a famous unsolved maths problem where if we took a positive number and if it is even we should divide by 2 else if it is odd then multiplication by 3 and adding 1 should be done. if we follow this pattern for any positive number the in always ends in 1
"""
def steps(number):
    """
    this function is used to calculate the number of steps that took a positive number to reach 1 using collatz conjecture. 
    raising a exception to point out that the given number should always be a positive integer. 
    step(int): it is a empty integer to store the no of steps that takes to convert a integer to 1 using collatz conjecture.
    """
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    step=0
    while number!=1:
        if number%2==0:
            number/=2
        else:
            number = (number*3)+1
        step+=1
    return step
