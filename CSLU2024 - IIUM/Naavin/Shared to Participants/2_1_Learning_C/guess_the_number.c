#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
	char messages[2][20] = {
		"Too high!",
		"Too low!",
	};
	srand(time(NULL));
	int number = rand() % 100 + 1;
	printf("I am thinking of a number between 1 and 100.\n");
	printf("Number is %d\n", number);
	int guess = 0;
	do {
		printf("What number am I thinking of? ");
		scanf("%d", &guess);
		int choice = guess < number;
		printf("%d is %s\n", guess, messages[choice]);
	} while (guess != number);
	printf("Yes! I was thinking of %d!\n", number);
	return 0;
}
