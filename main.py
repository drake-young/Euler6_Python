from timeit import default_timer

# ===========================================================
# PROBLEM 6 -- Sum square difference
# ===========================================================
#
# The sum of squares of the first ten natural numbers is:
#       1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the
# first hundred natural numbers and the suare of the sum
#
# ===========================================================
def problem_6( ):
    # Print the Problem Context
    print( "Project Euler Problem 6 -- Sum Square Difference" )

    # Set Up Variables
    start_time    =  default_timer( )
    sumOfSquares  =  0
    squareOfSum   =  0

    # Primary Loop -- compute all n^2 where 1<=n<=100, and compute the sum of those n
    for x in range( 1 , 101 ):
        sumOfSquares  +=  x * x
        squareOfSum   +=  x

    # Square the sum
    squareOfSum  *=  squareOfSum

    # Compute the Difference
    result  =  squareOfSum - sumOfSquares

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Difference between the sum of squares and the square of sums of first 100 natural numbers:   %d" % result )
    print( "   Computation Time:                                                                            %.3fms" % execution_time)
    return



if __name__ == '__main__':
    problem_6( )
