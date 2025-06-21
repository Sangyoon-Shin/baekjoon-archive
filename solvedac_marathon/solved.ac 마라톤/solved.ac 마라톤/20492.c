#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int money;

	scanf("%d", &money);
	printf("%d %d", money - money*22/100, money - money*20/100*22/100);

	return 0;
}