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
	if (h > 23) { // ���⸦ else if ������ �ع����� ���� ������ ������ ��쿡�� ����ǹǷ� �ð��� 23�� �Ѿ����.
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

		m += t; // �п� �丮 �ð��� ����
		h += m / 60; // �߰��� ���� �ð����� ��ȯ
		m %= 60; // ���� 60���� ���� ������

		h %= 24; // �ð��� 24�� ���� ������

		printf("%d %d", h, m);

		return 0;
	}
}

#endif
