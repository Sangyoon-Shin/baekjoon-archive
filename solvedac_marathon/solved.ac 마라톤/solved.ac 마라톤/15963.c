#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	long long a, b;

	scanf("%lld %lld", &a, &b);
	if (a == b) {
		printf("1");
	}
	else {
		printf("0");
	}

	return 0;
}