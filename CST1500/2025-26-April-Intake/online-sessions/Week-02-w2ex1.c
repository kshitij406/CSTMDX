#include <stdio.h>

int main(void)
{
	int x = 5;
	int y = 2; 
    int total = 0;
	char characterOne = 'a'; 
	char myString[] = ". That is Correct";

	printf("Add these 2 numbers: %d and %d", x, y);

    total = (x * y) + y;

    printf("\n\nThe total is: %d%s", total, myString);
	return 0;
}