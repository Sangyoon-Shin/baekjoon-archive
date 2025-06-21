#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int h, i, a, r, c;
	int first, second;

	scanf("%d %d %d %d %d", &h, &i, &a, &r, &c);
	first = h * i;
	second = a * r * c;

	int result = first - second;

	printf("%d", result);

	return 0;
}