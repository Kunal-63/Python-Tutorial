"""
Operators in Python:
1. Arithmetic Operator
    +
    -
    *
    /
    %       Modulo      Return remainder

        6 yrs
        10 months
        8 days

        2500 / 365 = 6
        2500 % 365 = 310
        310 / 30 = 10
        310 % 30 = 10
    //      Floor division/Integer division
    **      Exponent/Power

2. Logical Operators
    and
    or
    not

3. Conditional/Relational/Comparision Operators/Conditions
    These operators will always return you either True or False
    <
    >
    <=
    >=
    ==      :   Equality
    !=

4. Bitwise Operators
    &   Bitwise and
    |   Bitwise or

        3 : 0 0 1 1
        |
        5 : 0 1 0 1
            -------
            0 1 1 1 = 7

        Degree  Experience  Qualify?
        0       0           0
        0       1           1
        1       0           1
        1       1           1

    ~   Bitwise not

        5 : 0 1 0 1
        ~5: 1 0 1 0 = -6
    
    ^   Bitwise xor
    
        3 : 0 0 1 1
        ^
        5 : 0 1 0 1
            -------
            0 1 1 0 = 6

    <<  Bitwise left shift
        25 : 0 0 0 1  1 0 0 1
        << : 0 0 1 1  0 0 1 0 = 50
        << : 0 1 1 0  0 1 0 0 = 100

    >>  Bitwise right shift

5. Assignment Operators
    = 
        x = 5
        x = a + b
        
        a = 10
        b = 20
        a, b = b, a     Multiple Assignment
"""
print(2500/365)
print(2500//365)
print(5 ** 4)
print(round(2500/365, 3))
print(3 < 2)
print(3 | 5)
print(3 ^ 5)
print(25 << 3)

# Next Class: More assignment operators