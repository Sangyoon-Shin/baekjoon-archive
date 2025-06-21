#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char a[100], b[100];
	int c;

	scanf("%s %s %d", a, b, &c);

	int lena = strlen(a);
	int lenb = strlen(b);

	int aint = 0, bint = 0;


	for (int i = 0; i < lena; i++) {
		if (a[i] >= '0' && a[i] <= '9') {
			aint = aint * 10;
			aint = aint + a[i] - '0';
		}
	}

	for (int i = 0; i < lenb; i++) {
		if (b[i] >= '0' && b[i] <= '9') {
			bint = bint * 10;
			bint = bint + b[i] - '0';
		}
	}

	printf("%d\n", aint + bint - c);

	char* aptr = a;
	char* bptr = b;

	while (*aptr != '\0') {
		aptr++;
	}

	while (*bptr != '\0') {
		*aptr = *bptr;
		bptr++;
		aptr++;
	}
	*aptr = '\0';
	
	int lenaa = strlen(a);
	int res = 0;
	int result = 0;

	for (int i = 0; i < lenaa; i++) {
		if (a[i] >= '0' && a[i] <= '9') {
			res = res * 10;
			res = res + a[i] - '0';
		}
	}
	
	result = res - c;

	printf("%d", result);

	return 0;
}