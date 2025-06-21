#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int sum = 0;
	int score;

	for (int i = 0; i < 5; i++) {
		scanf("%d", &score);
		sum = sum + score;
	}

	printf("%d", sum);

	return 0;
}