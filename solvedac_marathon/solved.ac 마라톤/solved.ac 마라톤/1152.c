#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

char str[1000002];

int my_strlen(char *str) {
	
	int i = 0;
	while (*str != '\0') {
		i++;
		str++;
	}
	return i;
}

int main() {

	fgets(str, sizeof(str), stdin); // fgets 사용할때 sizeof(str)-1 개의 문자, \n, \0 을 순서대로 저장. 즉 필요공간의 +2만큼의 공간 필요

	int len = my_strlen(str);
	int cnt = 0;
	int start = 0;

	for (int i = 0; i < len; i++) {
		if (str[i] != ' ' && str[i] != '\n') {
			if (start == 0) {
				cnt++;
				start = 1;
			}
		}
		else {
			start = 0;
		}
	}

	printf("%d", cnt);

	return 0;
}