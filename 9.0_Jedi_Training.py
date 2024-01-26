# 9.0 Jedi Training (45pts)  Name:________________


#1.) Correct the following code and list corrections. (2pts)
# (The user's number should be increased by 1 and printed.)

def increase(x):
    return x + 1
 
num = input("Enter a number: ")
increase(x)
print("Your number has been increased to", x)

#1
#2
                        
 


#2.) Correct the following code to print 1-10:  (2pts)

def count_to_ten:
    for i in range[10]:
        print(i)
 
count_to_ten()

#1
#2


#3.) Correct the following code to sum the list:  (2pts)

def sum_list(list):
    for i in list:
        sum = i
        return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))

#1
#2


#4.) Correct the following code which should reverse the sentence that is entered.  (2pts)

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
    return result
 
text = input("Enter a sentence: ")
print(reverse(text))

#1
#2


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

##############################################################################
'''
Now that the functions have been created, use them all in a main program that will:
1.) Create a list of 10,000 random numbers from 1 to 6. (1 line of code)
2.) Print the count of 1 through 6. (For example, "There are 1361 amount of 2s") (3 lines of code)
3.) Print the average of all 10,000 random numbers. (Make sure it's a float) (2 lines of code)
'''
##############################################################################











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

