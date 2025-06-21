#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n, m;
	scanf("%d %d", &n, &m);
	if (n == 0 && m == 0) {
		return 0;
	}
	else {
		while (n !=0 || m != 0) {
			if (n > m) {
				printf("Yes\n");
				scanf("%d %d", &n, &m);
			}
			else {
				printf("No\n");
				scanf("%d %d", &n, &m);
			}
		}
	}

	return 0;
}