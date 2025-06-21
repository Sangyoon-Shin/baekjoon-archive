#if 0
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main(void) {
	int d1, d2, d3;
	int result;

	scanf("%d %d %d", &d1, &d2, &d3);

	if (d1 == d2 && d2 == d3) {
		result = 10000 + d1 * 1000;
		printf("%d", result);
	}

	else if (d1 == d2 || d1 == d3) {
		result = 1000 + d1 * 100;
		printf("%d", result);
	}

	else if (d2 == d3) {
		result = 1000 + d2 * 100;
		printf("%d", result);
	}

	else {
		if (d1 > d2 && d1 > d3) {
			result = d1*100;
			printf("%d", result);
		}
		else if (d2 > d1 && d2 > d3) {
			result = d2*100;
			printf("%d", result);
		}
		else if(d3 > d1 && d3 > d2){
			result = d3*100;
			printf("%d", result);
		}
	}
	return 0;
}
#endif
