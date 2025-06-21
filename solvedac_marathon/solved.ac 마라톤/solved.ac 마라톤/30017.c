#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int a, b;
	scanf("%d %d", &a, &b);

	if (a - 1 == b) {
		printf("%d", a + b);
	}
	else if (a > b) {
		printf("%d", 2 * b + 1);
	}
	else {
		printf("%d", 2 * a - 1);
	}

	return 0;
}