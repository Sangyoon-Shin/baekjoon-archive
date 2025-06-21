#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

	int n, num;
	scanf("%d", &n);
	scanf("%d", &num);

	int max = n * n;
	int xidx = 0, yidx = 0;

	int** data = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		data[i] = (int*)malloc(sizeof(int) * n);
	}



	int top = 0;
	int bottom = n - 1;
	int left = 0;
	int right = n - 1;
	while (max > 0) {
		for (int i = top; i <= bottom; i++) {
			data[i][left] = max;
			if (max == num) {
				xidx = i;
				yidx = left;
			}
			max--;
		}
		left++;
		for (int i = left; i <= right; i++) {
			data[bottom][i] = max;
			if (max == num) {
				xidx = bottom;
				yidx = i;
			}
			max--;
		}
		bottom--;
		for (int i = bottom; i >= top; i--) {
			data[i][right] = max;
			if (max == num) {
				xidx = i;
				yidx = right;
			}
			max--;
		}
		right--;
		for (int i = right; i >= left; i--) {
			data[top][i] = max;
			if (max == num) {
				xidx = top;
				yidx = i;
			}
			max--;
		}
		top++;
	}

	xidx = xidx + 1;
	yidx = yidx + 1;


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", data[i][j]);
		}
		printf("\n");
	}
	printf("%d %d", xidx, yidx);


	return 0;
}