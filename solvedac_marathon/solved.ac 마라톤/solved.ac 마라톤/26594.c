#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	char s[1000001];
	scanf("%s", s);

	int cnt = 0;
	char* sptr = s;
	char c = s[0];
	while (*sptr != '\0') {
		if (*sptr != c) {
			break;
		}
		sptr++;
		cnt++;
	}
	printf("%d", cnt);

	return 0;
}