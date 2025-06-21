#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int number[5];

	for (int i = 0; i < 5; i++) {
		scanf("%d", &number[i]);
	}

	printf("%d", (number[0] * number[0] + number[1] * number[1] + number[2] * number[2] + number[3] * number[3] + number[4] * number[4]) % 10);

	return 0;
}
