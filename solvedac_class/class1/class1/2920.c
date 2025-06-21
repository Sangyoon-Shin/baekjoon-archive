#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char a[9];
	char asc[9] = "12345678";
	char des[9] = "87654321";

	for (int i = 0; i < 8; i++) {
		scanf(" %c", &a[i]);
	}

	a[8] = '\0';

	if (strcmp(a, asc) == 0) {
		printf("ascending");
	}
	else if (strcmp(a, des) == 0) {
		printf("descending");
	}
	else {
		printf("mixed");
	}

	return 0;
}