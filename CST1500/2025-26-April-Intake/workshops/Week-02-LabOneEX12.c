#include <stdio.h>

// (Global - Scope) Variable declaration - no memory allocation - Can be seen by the whole program 

extern int a, b;
extern int c;
extern float f;

//extern int number = 9; //Is legal and does not cause an error

int main(void)
{
    /* (Local - Scope) Variable definition - no memory allocation */
    int a, b;
    int c;
    float f;

    /* actual initialization - memory is allocated*/
    a = 10;
    b = 20;
    c = a + b;

    printf("value of c : %d \n", c);

    f = 70.0 / 3.0;

    printf("value of f : %f \n", f);

    return 0;
}