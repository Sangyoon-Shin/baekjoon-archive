#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char a[1000];
	char b[1000];
	char sum[10000];

	scanf("%s", a);
	scanf("%s", b);

	int lenA = strlen(a);
	int lenB = strlen(b);
	int minlen = 0;

	if (lenA >= lenB) {
		 minlen = lenB;
	}
	else {
		minlen = lenA;
	}

	for (int i = 0; i < minlen; i++) {
		if (a[i] - '0' + b[i] -'0' < 10) {
			sum[i] = (a[i] - '0') + (b[i] - '0');
		}
		else {
			sum[i] = ((a[i] - '0' + b[i] - '0') / 10) + '0';
			sum[i + 1] = ((a[i] - '0' + b[i] - '0') % 10) + '0';
			sum[i + 2] = '\0';
		}
	}

	printf("%s", sum);

	return 0;
}