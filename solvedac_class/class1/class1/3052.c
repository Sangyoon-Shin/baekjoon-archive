#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int a[10];
	int cnt[1000] = { 0, };

	for (int i = 0; i < 10; i++) {
		scanf("%d", &a[i]);
	}

	for (int i = 0; i < 10; i++) {
		int rem = a[i] % 42;
		cnt[rem]++;
	}

	int count = 0;
	for (int i = 0; i < 1000; i++) {
		if (cnt[i] > 0) {
			count++;
		}
	}

	printf("%d", count);

	return 0;
}