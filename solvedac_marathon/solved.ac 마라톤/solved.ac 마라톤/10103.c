#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int scorea = 100, scoreb = 100;

	int a, b;
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {

		scanf("%d %d", &a, &b);
		if (a > b) {
			scoreb = scoreb - a;
		}
		else if (a < b) {
			scorea = scorea - b;
		}
	}
	printf("%d %d", scorea, scoreb);

	return 0;
}