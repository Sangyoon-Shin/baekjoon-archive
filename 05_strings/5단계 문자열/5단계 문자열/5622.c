#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char str[16];
	scanf("%s", str);

	int len = strlen(str);
	int time = 0;

	for (int i = 0; i < len; i++) {
		if (str[i] >= 'A' && str[i] <= 'C') {
			time = time + 3;
		}
		else if (str[i] >= 'D' && str[i] <= 'F') {
			time = time + 4;
		}
		else if (str[i] >= 'G' && str[i] <= 'I') {
			time = time + 5;
		}
		else if (str[i] >= 'J' && str[i] <= 'L') {
			time = time + 6;
		}
		else if (str[i] >= 'M' && str[i] <= 'O') {
			time = time + 7;
		}
		else if (str[i] >= 'P' && str[i] <= 'S') {
			time = time + 8;
		}
		else if (str[i] >= 'T' && str[i] <= 'V') {
			time = time + 9;
		}
		else if (str[i] >= 'W' && str[i] <= 'Z') {
			time = time + 10;
		}
	}
	
	printf("%d", time);

	return 0;
}