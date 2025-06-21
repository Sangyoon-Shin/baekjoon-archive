#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	unsigned short year;
	scanf("%hu", &year);
	if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
		printf("1");
	}
	else if (year == 0||year>4000) {
		printf("error");
	}
	else {
		printf("0");
	}

	return 0;
}
#endif
