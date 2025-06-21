#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	long long n;
	long long factorial = 1;

	scanf("%lld", &n);
	if (n <= 1) {
		printf("1");
		return 0;
	}
	else {
		for (int i = 1; i <= n; i++) {
			factorial = factorial * i;
		}
		printf("%lld", factorial);
	}

	return 0;
}