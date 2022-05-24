# COSC140 lab 5

## Lab feedback

 * How long did you spend on this lab?

 * What did you think about it?  What was good?  What could be improved?

## Feedback

S/N

Most everything works well.  One problem when an invalid rating is given is that the form re-renders without any of the error/validation information.  If you avoid creating a new form object and just use the one that was used for validation the errors will correctly render.  You've also got duplicate lookups of the product object in that function which are unnecessary.

