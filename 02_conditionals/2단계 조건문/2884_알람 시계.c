#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int h,m;
	scanf("%d %d", &h, &m);
	if (m >= 45) {
		printf("%d %d", h, m - 45);
	}
	else if (h == 0 ) {
		printf("%d %d", 23, m + 15);
	}
	else {
		printf("%d %d", h - 1, m + 15);
	}
	return 0;
}
#endif
