#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	char str[51];
	int len;

	int r = 31;
	int m = 1234567891;

	scanf("%d", &len);
	scanf("%s", str);


	long long result = 0;
	int square[50] = { 1, };
	for (int j = 1; j < len; j++) {
		square[j] = square[j - 1] * r;
	}

	for (int i = 0; i < len; i++) {
		result += ((((str[i] - 'a' + 1) * square[i]) %m)) %m;
	}
	result %= m;

	printf("%lld", result);



	return 0;
}