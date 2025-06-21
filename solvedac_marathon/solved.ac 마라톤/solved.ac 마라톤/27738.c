#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	unsigned long x = 0;
	unsigned long n;
	unsigned long arr[6] = { 0, };
	scanf("%ld", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%ld", &arr[i]);
	}

	for (unsigned long i = 1; i <= n; i++) {
		if (i % arr[0] == 0) {
			x = x + i;
		}
		if (i % arr[1] == 0) {
			x = x % i;
		}
		if (i % arr[2] == 0) {
			x = x & i;
		}
		if (i % arr[3] == 0) {
			x = x ^ i;
		}
		if (i % arr[4] == 0) {
			x = x | i;
		}
		if (i % arr[5] == 0) {
			x = x >> i;	
		}
	}
	printf("%ld", x);

	return 0;
}