#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	unsigned short score;
	scanf("%hu", &score);
	if (score <= 100 && score >= 90) {
		printf("A");
	}
	else if (score >= 80) {
		printf("B");
	}
	else if (score >= 70) {
		printf("C");
	}
	else if (score >= 60) {
		printf("D");
	}
	else {
		printf("F");
	}
	return 0;
}
#endif
