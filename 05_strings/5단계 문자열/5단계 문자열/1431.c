#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int my_strcmp(char* s1, char* s2) {

	while (*s1 != '\0' || *s2 != '\0') {
		if (*s1 > *s2) {
			return *s1 - *s2;
		}
		else if (*s1 < *s2) {
			return *s1 - *s2;
		}
		s1++;
		s2++;
	}
	return *s1 - *s2;
}

int main() {

	int n;
	char serial[50][52];

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", serial[i]);
	}

	for (int i = 1; i < n; i++) {
		char key[52];
		strcpy(key, serial[i]);
		for (int j = i; j >= 0; j--) {
			if (strlen(key) < strlen(serial[j])) {
				strcpy(serial[j + 1], serial[j]);
				strcpy(serial[j], key);
			}
			else if (strlen(key) == strlen(serial[j])) {
				int cntkey = 0;
				int cntserial = 0;
				for (int k = 0; k < strlen(key); k++) {
					if (key[k] >= '0' && key[k] <= '9') {
						cntkey = cntkey + (key[k] - '0');
					}
					if (serial[j][k] >= '0' && serial[j][k] <= '9') {
						cntserial = cntserial + (serial[j][k] - '0');
					}
				}
				if (cntkey < cntserial) {
					strcpy(serial[j + 1], serial[j]);
					strcpy(serial[j], key);
				}
				else if (cntkey == cntserial) {
					if (my_strcmp(key, serial[j]) < 0) {
						strcpy(serial[j + 1], serial[j]);
						strcpy(serial[j], key);
					}
				}
			}
		}
	}

	for (int i = 0; i < n; i++) {
		printf("%s\n", serial[i]);
	}

	return 0;
}