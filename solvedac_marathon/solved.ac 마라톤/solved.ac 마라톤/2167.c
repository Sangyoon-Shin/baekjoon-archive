#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

	int n, m;
	scanf("%d %d", &n, &m);

	int** arr = NULL;
	arr = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		arr[i] = (int*)malloc(sizeof(int) * m);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf(" %d", &arr[i][j]);
		}
	}

	int k, a, b, x, y;
	scanf("%d", &k);


	for (int l = 0; l < k; l++) {
		scanf("%d %d %d %d", &a, &b, &x, &y);
		int sum = 0;
		for (int i = a - 1; i <= x - 1; i++) {
			for (int j = b - 1; j <= y - 1; j++) {
				sum = sum + arr[i][j];
			}
		}
		printf("%d\n", sum);
	}

	for (int i = 0; i < n; i++) {
		free(arr[i]);
	}
	free(arr);

	return 0;
}