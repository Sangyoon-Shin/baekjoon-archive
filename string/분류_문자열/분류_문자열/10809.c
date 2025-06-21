#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int* findFirstLocation(char* str, int* location) {

	char* start = str;
	while (*str != '\0') {
		if (location[*str - 'a'] == -1) {
			location[*str - 'a'] = str - start;
		}
		str++;
	}
	return location;
}

int main() {

	char str[101];
	int location[26];
	for (int i = 0; i < 26; i++) {
		location[i] = -1;
	}
	scanf("%s", str);
	findFirstLocation(str, location);
	for (int i = 0; i < 26; i++) {
		printf("%d ", location[i]);
	}

	return 0;
}