/*  EX10 Week 3 lab worksheet
    Program to calculate the sum of first n natural numbers
    Positive integers 1,2,3...n are known as natural numbers */

#include <stdio.h>

int main(void)
{
    // Variable declaration and assignment
    int num, count, sum = 0;

    // Prompt for user input
    printf("Enter a positive integer: ");

    // Assign the value input by the user to the num variable using the
    //  %d format specifier. The & indicates where to save the value in memory.
    //  In this instance, save the input value to the memory allocated to the num variable.
    scanf("%d", &num);

    // for loop terminates when num is less than count
    // Start the value of count at 1.
    // For each time you want the code to be executed:
    // a) Check if the value of count is less than or equal to the value of num.
    // If the value of count is less than or equal to the value of num:
    // b) Execute the code.

    // If the value of count is more than the value of num:
    // Exit the for loop and continue with the next line of code after the for loop.

    // C) Finally, add 1 to the count variable.
    // d) Go to a).

    for (count = 1; count <= num; ++count)
    {
        sum += count;
        printf("\nCurrent value of sum: %d", sum);
        printf("\nCurrent value of count: %d", count);
    }

    printf("\nCurrent value of count: %d", count);
    // Print the statement to the terminal using the format specifier %d
    // The variable which follows the , will 'replace' the format specifier %d.
    // Variable sum - in this instance.
    printf("\nSum = %d", sum);

    // NOTES: The \n creates a new line or a return. Placement of the \n is important for formatting.
    // a += b is the same as a = a + b
    // ++ basically adds 1 to the variable e.g. ++count  

    return 0;
}