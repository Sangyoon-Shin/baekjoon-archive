#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int t;
	int h, w, n;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		int height = 0, width = 0;
		scanf("%d %d %d", &h, &w, &n);
		width = n / h;
		height = n % h;
		if (n % h == 0) {
			printf("%d%02d\n", h, width);
		}
		else {
			printf("%d%02d\n", height, 1 + width);
		}
	}

	return 0;
}