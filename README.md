# Simple-Calculator

This is a small project written in Python 3.7.
It is a simple calculator. To use it, simply enter 
your calculation by pressing ENTER after each element (number or operator).
The calculation will have a vertical look to it (see example).
Write a '=' in order to display the result. After a result has been displayed,
the loop restarts and you can enter a new calculation.

<b>Structure of the input:</b>

<em>number</em>

<em>operator</em>

<em>number</em>

...

<em>equalsign</em>

<b>OUTPUT</b>

<em>result </em>

===================

<b>NOTE:</b> Because of it's simplicity, this calculator does not include operator precedence.
If your calculation includes multiplications or divisions, calculate those expressions seperately and then 
use the results of those expressions inside your original calculation, in order for it to be calculated correctly.

===================

<b>Optimization: </b>

When I wrote this program, I did not yet know the evaluate function eval() which comes with Python 3.7 and allows for 
a much more complete, efficient aswell as elegant calculator, all in one line of code:

> print(eval(input("Enter Calculation: ")))






