# 9.0 Jedi Training (45pts)  Name:________________


#1.) Correct the following code and list corrections. (2pts)
# (The user's number should be increased by 1 and printed.)

def increase(x):
    result = int(x) + 1
    return result
 
num = input("Enter a number: ")
print("Your number has been increased to", increase(num))

#1: x is the template parameter, it is not actually defined and another real variable should be used. num should be the function input.
#2: because x is the template parameter another real variable is needed instead. In my instance, I moved the increase function to the inside of the print function.
                        
 


#2.) Correct the following code to print 1-10:  (2pts)

def count_to_ten():
    for i in range(10):
        print(i)
 
count_to_ten()

#1: every function has to have parenthesis even if they are empty. functions are called by including the parenthesis [Ex: fun()]
#2: the range function is a function which requires a parenthesis to input the parameters, in this case the range of numbers


#3.) Correct the following code to sum the list:  (2pts)

def sum_list(nums):
    list_sum = 0
    for i in nums:
        list_sum += i
        return list_sum
 
lists = [45, 2, 10, -5, 100]
print(sum_list(lists))

#1: the sum needs to be defined outside the for loop for the number to be added. I defined it as 0.
#2 i must be added to the sum, unlike
#Extra: Naming collisions exist with the given variable names. As such I changed them all to unused variables.

#4.) Correct the following code which should reverse the sentence that is entered.  (2pts)

def reverse(string):
    result = ""
    text_length = len(string)
    for i in range(text_length):
        result += string[-i - 1]
    return result

text = input("Enter a sentence: ")
print(reverse(text))

#1: the function needs a different variable than one from the outer scope. I adjusted it to string
#2: In order to reverse the list you need to not only make i negative to go backwards through the string, but you also need to minus it by one because lists start at 0 and -0 == 0.


##############################################################################
'''
#5.) MINI FUNCTION (2pts)
-------------------------------
Write a function called mini that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))

OUTPUT
------
3
4
2
-100
A

The function should return the value, not print the value. 
Also, while there is a min function built into Python, don't use it. 
Please use if statements and practice creating it yourself.
'''
##############################################################################
def mini(x, y, z):
    lowest = x
    items = [y, z]
    for i in items:
        if i <= lowest:
            lowest = i
    return lowest
##############################################################################
'''
6.) BOX_FUNCTION (2pts)
-------------------------------
Write a function called box that will output boxes (made of lower case o's) 
given a height and width. Once you've finished writing your function, copy 
and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
box(7,5) # Print a box 7 high, 5 across
print() # Blank line
box(3,2) # Print a box 3 high, 2 across
print() # Blank line
box(3,10) # Print a box 3 high, 10 across

OUTPUT
------
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo

oo
oo
oo

oooooooooo
oooooooooo
oooooooooo
'''
##############################################################################
def box(height, length):
    string = ""
    for i in range(length):
        string += "o"
    for i in range(height):
        print(string)
##############################################################################
'''
7.) FIND FUNCTION (2pts)
-------------------------------
Write a function called FIND that will take a list of numbers, "list", 
along with one other number, "key". Have it search the list for the value
contained in key. Each time your function finds the key value, 
print the list position of the key. You will need to juggle three variables,
one for the list, one for the key, and one for the position of where you are 
in the list. You may want to review your notes for the code to iterate though
a list using the range and len functions. Start with that code and modify the 
print to show each element and its position. Then instead of just printing 
each number, add an if statement to only print the ones we care about. 
Once you've finished writing your function, copy and paste the following code 
after it and make sure it works with the function you wrote:

INPUT
-----
list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(list, 12)
find(list, 91)
find(list, 80)

OUTPUT
------
Found 12 at position 11
Found 12 at position 13
Found 91 at position 5

Use a for loop with an index variable and a range. 
Inside the loop use an if statement. This function 
can be written in about four lines of code.
'''
##############################################################################
def find(array, key):
    for i in range(len(array)):
        if key == array[i]:
            print(f"Found {key} at position {i}")
##############################################################################
'''
8.) FIZZBUZZ (3pts)
-------------------------------
The "Fizz-Buzz test" is an interview question designed to help filter out the 99.5% 
of programming job candidates who can't seem to program their way out of a wet paper bag.
Write a function called fizzbuzz that prints the numbers from 1 to "endpoint", where 
endpoint is your final number. But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz". The classic test is to use the numbers 1-100 so make
sure you test that with your function.
'''
##############################################################################
def fizzbuzz(limit):
    for i in range(1, limit + 1): #Done to actually include limit
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
##############################################################################
'''
9.) FIBONACCI (3pts)
-------------------------------
In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, 
called the Fibonacci sequence, and characterized by the fact that every number after the
first two is the sum of the two preceding ones:1,1,2,3,5,8,13,21,34,55,89,144
Write a function called fibonacci() that will print up to a maximum of the first 100 numbers
in the Fibonacci sequence. Pass the number into the function.
'''
##############################################################################
def fibonaci(limit):
    if limit > 100:
        limit = 100
    a = 1
    b = 0
    result = 0
    for i in range(1, limit + 1):
        if i == 1:
            print(1)
        else:
            result = a + b
            print(result)
            if i % 2 == 0:
                b = result
            else:
                a = result
##############################################################################
'''
10.) 10,000 NUMBERS (15pts)
-------------------------------

In this program we will write three different functions.

Function #1: Write a function named create_list that takes
in a list size and returns a list of random numbers from 1-6.
i.e., calling create_list(5) should return 5 random numbers from 1-6.
Once you've finished writing your function, copy and paste the
following code after it and make sure it works with the function you wrote:

INPUT
-----
my_list = create_list(5)
print(my_list)

OUTPUT
------
[2,5,1,6,3] #something like this 
'''
##############################################################################
import random

def create_list(buffer):
    randlist = []
    for i in range(buffer):
        r = random.randint(1, 6)
        randlist.append(r)
    return randlist
##############################################################################
'''
Function #2: Write a function called count_list that takes
in your previous list and a number. Have the function return the amount
of times the specified number appears in the list. Once you've
finished writing your function, copy and paste the following code
after it and make sure it works with the function you wrote:

INPUT
-----
my_list = [1,2,3,3,3,4,2,1]
count = count_list(my_list,3)
print(count)

OUTPUT
------
3 
'''
##############################################################################
def count_list(array, num):
    tally = 0
    for value in array:
        if value == num:
            tally += 1
        else:
            continue
    return tally
##############################################################################
'''
Function #3: Write a function called average_list that returns the 
average of your previous list passed into it. Once you've finished writing your
function, copy and paste the following code after it and make sure it
works with the function you wrote:

INPUT
-----
my_list = [1,2,3]
avg = average_list(my_list)
print(avg)

OUTPUT
------
2.0
'''
##############################################################################
def average_list(array):
    total = 0
    for value in array:
        total += value
    return total / len(array)
##############################################################################
'''
Now that the functions have been created, use them all in a main program that will:
1.) Create a list of 10,000 random numbers from 1 to 6. (1 line of code)
2.) Print the count of 1 through 6. (For example, "There are 1361 amount of 2s") (3 lines of code)
3.) Print the average of all 10,000 random numbers. (Make sure it's a float) (2 lines of code)
'''
##############################################################################
tenThousand = create_list(10000)
for i in range(1, 7):
    runningTotal = count_list(tenThousand, i)
    print(f"There are {runningTotal} amount of {i}s")
mean = float(average_list(tenThousand))
print(f"The average number in the list is {mean}")
##############################################################################
'''
11.) BB8 DRAWING PROGRAM (10pts)
-------------------------------
Back to the drawing board! Get it? Let's say we want to draw many BB8 robots
of varying sizes at various locations. We can make a function called draw_BB8().
We've made some basic changes to our original drawing program. We still have the
first two lines as importing arcade and opening an arcade window. We actually took 
all of the other drawing code and put it in a function called main(). At the bottom
we call the main() function. In the main() function we call the draw_BB8() function
multiple times. We pass three parameters to it: x, y and radius. Write the code for 
the draw_BB8() function so that the resulting picture looks as close as you can get
it to the one on the website.
'''

# Imports arcade module
import arcade

# Opens a 600px by 600px window and puts BB8 in the title
arcade.open_window(600, 600, "BB8")

# Function to draw BB8 robots
def draw_BB8(x,y, radius):
    arcade.draw_rectangle_filled(x - (0.33 * radius), y + (1.66 * radius), radius * 0.1, radius * 0.5, arcade.color.BLACK, 0)
    arcade.draw_rectangle_filled(x, y + (1.25 * radius), radius * 1.25, radius * 0.66, arcade.color.WHITE, 0)
    arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE, 0, 64)
    arcade.draw_circle_filled(x, y, radius * 0.7, arcade.color.LIGHT_GRAY, 0, 64)
    arcade.draw_rectangle_filled(x, y, 1.25 * radius, radius * 0.2, arcade.color.GRAY, 0)
    arcade.draw_circle_outline(x, y, (radius * 0.75), arcade.color.ORANGE, 12 * (radius / 50), 0, 64)
    arcade.draw_circle_filled(x, y + (1.25 * radius), radius * 0.2, arcade.color.BLACK, 0, 64)

# The main function where we set background color, start and finish rendering and run.
def main():
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()

    draw_BB8(100,50,50)
    draw_BB8(300, 300, 30)
    draw_BB8(500, 100, 20)
    draw_BB8(500, 400, 60)
    draw_BB8(120, 500, 15)

    arcade.finish_render()
    arcade.run()

# Calls the main function
if __name__=="__main__":
    main()

