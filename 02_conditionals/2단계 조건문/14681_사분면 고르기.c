#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int x, y;
	scanf("%d", &x);
	scanf("%d", &y);

	if (x > 0 && y > 0) {
		printf("1");
	}
	else if (x < 0 && y>0) {
		printf("2");
	}
	else if (x < 0 && y < 0) {
		printf("3");
	}
	else if (x > 0 && y < 0) {
		printf("4");
	}
	else if (x == 0 || y == 0) {
		printf("error.");
	}

	return 0;
}
#endif
