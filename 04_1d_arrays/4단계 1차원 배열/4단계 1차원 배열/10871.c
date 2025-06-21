#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#define MAX 10000

int main(void) {

	int array[MAX] = { 0, };
	int NA;
	int cmp;

	scanf("%d %d", &NA, &cmp);
	for (int i = 0; i < NA; i++) {
		scanf("%d", &array[i]);
	}
	for (int i = 0; i < NA; i++) {
		if (array[i] < cmp) {
			printf("%d ", array[i]);
		}
	}

	return 0;
}