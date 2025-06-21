#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	int n;
	char** str = (char**)malloc(sizeof(char*) * n);
	for (int i = 0; i < n; i++) {
		str[i] = (char*)malloc(sizeof(char) * 52);
	}

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %s", str[i]);
	}

	for (int i = 1; i < n; i++) {
		char key[52];
		strcpy(key, str[i]);
		for (int j = i; j >= 0; j--) {
			if (strcmp(key, str[j]) > 0) {
				strcpy(str[j + 1], str[j]);
				strcpy(str[j], key);
			}
		}
	}

	for (int i = 0; i < n; i++) {
		printf("%s\n", str[i]);
	}

	return 0;
}