#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int x, y, z;

	while (1) {
		scanf("%d %d %d", &x, &y, &z);
		if (x == 0 && y == 0 && z == 0) {
			break;
		}
		else if (x == y == z) {
			printf("wrong\n");
		}
		else if (x * x == y * y + z * z || y * y == x * x + z * z || z * z == x * x + y * y) {
			if (x == 0 || y == 0 || z == 0) {
				printf("wrong\n");
			}
			else {
				printf("right\n");
			}
		}
		else {
			printf("wrong\n");
		}
	}

	return 0;
}