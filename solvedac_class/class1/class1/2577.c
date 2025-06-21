#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	unsigned int a, b, c;
	scanf("%u %u %u", &a, &b, &c);

	unsigned int product = a * b * c;

	char num[20];
	int count[10] = { 0, };

	sprintf(num, "%d", product); // atoi는 표준함수 아님

	for (int i = 0; i < strlen(num); i++) {
		count[num[i] -'0']++;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d\n", count[i]);
	}

	return 0;
}