#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void hailstone(int n) {
	int max = n;
	if (n == 1) {
		printf("1\n");
		return;
	}
	while (n != 1) {
		if (n % 2 == 0) {
			n = n / 2;
			if (n >= max) {
				max = n;
			}
		}
		else {
			n = n * 3 + 1;
			if (n >= max) {
				max = n;
			}
		}
	}
	printf("%d\n", max);
}

int main(void) {

	int n, T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d", &n);
		hailstone(n);
	}

	return 0;
}