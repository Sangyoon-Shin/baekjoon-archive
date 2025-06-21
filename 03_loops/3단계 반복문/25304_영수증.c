#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int total, category, price, num;
	int result[101];
	int total_result = 0;
	scanf("%d", &total);
	scanf("%d", &category);

	for (int i = 0; i < category; i++) {
		scanf("%d %d", &price, &num);
		result[i] = price * num;
	}

	for (int i = 0; i < category; i++) {
		total_result = total_result + result[i];
	}

	if (total_result == total) {
		printf("Yes\n");
	}
	else {
		printf("No\n");
	}
	return 0;
}
#endif

