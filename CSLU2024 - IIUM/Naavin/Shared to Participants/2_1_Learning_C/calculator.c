#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {return a+b;}
int subtract(int a, int b) {return a-b;}
int divide(int a, int b) {return a/b;}
int multiple(int a, int b) {return a*b;}

int main(int argc, char* argv[]) {
	if (argc != 4)  {
		printf("Usage: %s <number1> <+ or - or / or *> <number2>\n", argv[0]);
		return -1;
	}
	// Convert the string to an int
	int number1 = atoi(argv[1]);
	int number2 = atoi(argv[3]);
	int result = 0;
	switch (argv[2][0]) {
		case '+':
			// I use function calls so that
			// you can see later on how it looks
			// like in Assembly
			result = add(number1, number2);
			break;
		case '-':
			result = subtract(number1, number2);
			break;
		case '*':
			result = multiple(number1, number2);
			break;
		case '/':
			result = divide(number1, number2);
			break;
	}
	printf("%d %c %d = %d\n", number1, argv[2][0] ,number2, result);
	return 0;
}
