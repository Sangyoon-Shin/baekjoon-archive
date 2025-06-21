#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int score[5];
	int sum = 0;

	for (int i = 0; i < 5; i++) {
		scanf("%d", &score[i]);
		if (score[i] >= 40) {
			sum = sum + score[i];
		}
		else {
			sum = sum + 40;
		}
	}

	printf("%d", sum/5);

	return 0;
}