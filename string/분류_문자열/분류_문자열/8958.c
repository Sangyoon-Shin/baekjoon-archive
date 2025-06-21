#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int getScore(char* str) {

	int score = 0;
	int cnt = 0;

	while (*str != '\0') {
		if (*str == 'O') {
			cnt++;
			score = score + cnt;
		}
		else {
			cnt = 0;
		}

		str++;
	}
	return score;
}

int main() {

	char str[80];
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%s", str);
		printf("%d\n", getScore(str));
	}

	return 0;
}