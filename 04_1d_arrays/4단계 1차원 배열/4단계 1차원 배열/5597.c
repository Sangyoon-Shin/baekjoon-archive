#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n = 0;
	int list[31] = { 0, };	// üũ����Ʈ ��� 0���� �ʱ�ȭ

	int xlist[2] = { 0, }; // ���� ���� �ֵ� ��ȣ ������ �迭

	int idx = 1; // list�� �ε��� ��Ÿ�� ��. ��ȣ�� 1�����ʹϱ� �ʱⰪ 1
	int xidx = 0; // list���� ���� 0�� �ε����� �����ϱ� ���� �迭�� �ε��� ��Ÿ���� ����.

	for (int i = 0; i < 28; i++) { 
		scanf("%d", &n);	
		list[n] = 1;	
	}

	do {
		if (list[idx] == 0) { // �����ܿ��� ���� 0�� �ε����� ã��
			xlist[xidx] = idx;
			xidx++;
		}
		idx++;
	} while (idx != 31);

	printf("%d\n%d", xlist[0], xlist[1]);
	

	return 0;
}