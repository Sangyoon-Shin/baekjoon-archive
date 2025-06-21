#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;
	char number[101];
	int result = 0;

	scanf("%d", &n);
	scanf("%s", number);

	for (int i = 0; i < n; i++) {
		result = result + number[i] - '0';
	}

	printf("%d", result);

	return 0;
}