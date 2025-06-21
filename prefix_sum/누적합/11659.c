#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	unsigned int n, m,num,sum = 0;
	unsigned int _sum[100000] = { 0, };

	scanf("%u %u", &n, &m);
	// sum[0] = 0
	for (int i = 1; i <= n; i++) {
		scanf("%d", &num);
		sum += num;
		_sum[i] = sum;
	}

	// 1 3 -> 12 - 0 -> [3] - [0]
	int x, y;
	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		x--;
		int p = _sum[y] - _sum[x];
		printf("%d\n", p);
	}
	
	return 0;
}