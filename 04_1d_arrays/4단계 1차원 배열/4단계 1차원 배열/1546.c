#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;
	double max = 0;
	double score[1000]; // ���� ���� ������ �迭
	double new_score[1000];	// ������ ���� ������ �迭
	double sum = 0; // ������ �������� �� ������ ����
	double new_avg = 0;	// ������ �������� ��� ��Ÿ�� ����

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &score[i]);	
		if (score[i] >= max) {	// ���� ���� �߿��� �ִ밪 ���ϱ�
			max = score[i];
		}
	}

	for (int i = 0; i < n; i++) {
		new_score[i] = score[i] * 1 / max * 100; // ������ ��Ÿ�� ���� �����Ų ������ ���ο� �迭�� ����
		sum = sum + new_score[i];	// ���ο� �迭�� ��� ������ ��
	}

	new_avg = sum / n; // ������ ������ ��� ���ϱ�

	printf("%lf", new_avg);

	return 0;
}