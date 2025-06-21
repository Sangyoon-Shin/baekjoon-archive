#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;
	int sum = 0;
	int square;
	int cube = 0;

	scanf("%d", &n);
	
	if (n < 5 || n>100) {
		return 0;
	}
	else {
		for (int i = 1; i <= n; i++) {
			sum = sum + i;
			cube = cube + i * i * i;
		}
		square = sum * sum;
		printf("%d\n%d\n%d", sum, square, cube);
	}

	return 0;
}