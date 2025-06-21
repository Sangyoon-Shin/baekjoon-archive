#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int h, m, t;
	int a;

	scanf("%d %d", &h, &m);
	scanf("%d", &t);

	if (m + t < 60) {
		a = m + t;
	}
	else if (m + t == 60) {
		a = (m + t) % 60;
		h = h + 1;
		if (h > 23) {
			h = h % 24;
		}
		if (m > 59) {
			a = m % 60;
			h = h + m / 60;
		}
	}
	else if (m + t > 60) {
		a = (m + t) % 60;
		h = h + (m + t) / 60;

	}
	if (h > 23) { // 여기를 else if 문으로 해버리면 위에 조건이 거짓인 경우에만 실행되므로 시간이 23을 넘어가버림.
		h = h % 24;
	}
	if (m > 59) {
		a = m % 60;
		h = h + m / 60;
	}

	printf("%d %d", h, a);

	return 0;
}

#if 0
int main() {
#include <stdio.h>

	int main(void) {
		int h, m, t, a;

		scanf("%d %d", &h, &m);
		scanf("%d", &t);

		m += t; // 분에 요리 시간을 더함
		h += m / 60; // 추가된 분을 시간으로 변환
		m %= 60; // 분은 60으로 나눈 나머지

		h %= 24; // 시간은 24로 나눈 나머지

		printf("%d %d", h, m);

		return 0;
	}
}

#endif
