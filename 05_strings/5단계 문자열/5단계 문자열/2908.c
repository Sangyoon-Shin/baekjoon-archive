#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	char num1[4];
	char num2[4];

	scanf("%s %s", num1, num2);

	int realnum1 = 0, realnum2 = 0;

	for (int i = 2; i >=0; i--) {
		realnum1 = realnum1 * 10;
		realnum1 = realnum1 + (num1[i] - '0');
		realnum2 = realnum2 * 10;
		realnum2 = realnum2 + (num2[i] - '0');
	}
	if (realnum1 > realnum2) {
		printf("%d", realnum1);
	}
	else {
		printf("%d", realnum2);
	}

	return 0;
}