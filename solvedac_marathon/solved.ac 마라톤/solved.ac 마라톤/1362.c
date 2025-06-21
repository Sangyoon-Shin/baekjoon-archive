#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int fit, real, n;
	char control;
	int flag = 0;

	scanf("%d %d", &fit, &real);
	if (fit == 0 && real == 0) {
		return 0;
	}
	while (1) {
		scanf("%c %d", &control, &n);
		if (flag == -1) {
			continue;
		}
		if (control == 'F') {
			real = real - n;
		}
		if (control == 'E') {
			real = real + n;
		}
		if (control == '#' && n == 0) {
			if (flag == 1) {
				printf(":-\)\n");
			}
			else if (flag == 0) {
				printf(":-\(\n");
			}
			else {
				printf("RIP\n");
			}
			scanf("%d %d", &fit, &real);
			if (fit == 0 && real == 0) {
				break;
			}
		}
		if ((real > (fit / 2)) && (real < (fit * 2))) {
			flag = 1;
		}
		else if (real <= 0) {
			flag = -1;
		}
		else{
			flag = 0;
		}
	}



	return 0;
}