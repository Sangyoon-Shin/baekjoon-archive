#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#if 0
int strlen(char* str) {
	int i = 0;
	while (*str != '\0') {
		i++;
		str++;
	}
	return i;
}

int main() {

	char str[100000];

	while (1) {
		scanf("%s", str);
		if (str[0] == '0' && str[1] == '\0') {
			break;
		}
		int len = strlen(str);
		int start = 0;
		int end = len - 1;
		int flag = 1;
		while (start < end) {
			if (str[start] != str[end]) {
				flag = 0;
				break;
			}
			else {
				start++;
				end--;
			}
		}
		if (flag == 1) {
			printf("yes\n");
		}
		else {
			printf("no\n");
		}
	}

	return 0;
}
#endif


int strlen(char* str) {
	int i = 0;
	while (*str != '\0') {
		i++;
		str++;
	}
	return i;
}

int main() {

	// 이 코드는 한 자릿수면 while문 돌지 못하고 flag가 0으로 설정된 상태에서 끝남.

	char str[100000];

	while (1) {
		scanf("%s", str);
		if (str[0] == '0' && str[1] == '\0') {
			break;
		}
		int len = strlen(str);
		int start = 0;
		int end = len - 1;
		int flag = 0;
		while (start < end) {
			if (str[start] == str[end]) {
				flag = 1;
				start++;
				end--;
			}
			else {
				flag = 0;
				break;
			}
		}
		if (flag == 1) {
			printf("yes\n");
		}
		else {
			printf("no\n");
		}
	}

	return 0;
}
