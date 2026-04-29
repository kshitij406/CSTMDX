#include <stdio.h>

int main(void)
{
    // only the variable with a * is a pointer here. c and d are normal variables
    int *pc, c, d;
    
    c = 5;
    d = -15;

    // assign the memory address of the variable c to the pointer pc  
    pc = &c;

    printf("\nThe *pc pointer is pointing to the value of c: %d", *pc); 
    
    // assign the memory address of the variable d to the pointer pc  
    pc = &d;
    printf("\nThe *pc pointer is pointing to the value of d: %d", *pc); 

    return 0;
}