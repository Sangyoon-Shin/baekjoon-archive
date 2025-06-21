#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int	king, queen, look, bshawp, knight, pawn;
	int cntKing = 0;
	int cntQueen = 0; 
	int cntLook = 0;
	int cntBshawp = 0;
	int cntKnight = 0;
	int cntPawn = 0;

	scanf("%d %d %d %d %d %d", &king, &queen, &look, &bshawp, &knight, &pawn);

	if (king == 1 && queen == 1 && look == 2 && bshawp == 2 && knight == 2 && pawn == 8) {
		printf("%d %d %d %d %d %d", cntKing, cntQueen, cntLook, cntBshawp, cntKnight, cntPawn);
	}
	else if(king > 1 || queen > 1 || look > 2 || bshawp > 2 || knight > 2 || pawn > 8){
		while (king != 1) {
			cntKing--;
			king--;
		}
		while (queen != 1) {
			cntQueen--;
			queen--;
		}
		while (look != 2) {
			cntLook--;
			look--;
		}
		while (bshawp != 2) {
			cntBshawp--;
			bshawp--;
		}
		while (knight != 2) {
			cntKnight--;
			knight--;
		}
		while (pawn != 8) {
			cntPawn--;
			pawn--;
		}

		printf("%d %d %d %d %d %d", cntKing, cntQueen, cntLook, cntBshawp, cntKnight, cntPawn);
	}
	else {
		while (king != 1) {
			cntKing++;
			king++;
		}
		while (queen != 1) {
			cntQueen++;
			queen++;
		}
		while (look != 2) {
			cntLook++;
			look++;
		}
		while (bshawp != 2) {
			cntBshawp++;
			bshawp++;
		}
		while (knight != 2) {
			cntKnight++;
			knight++;
		}
		while (pawn != 8) {
			cntPawn++;
			pawn++;
		}
		printf("%d %d %d %d %d %d", cntKing, cntQueen, cntLook, cntBshawp, cntKnight, cntPawn);
	}

	return 0;
}



#if 0
#include <stdio.h>

int main() {
	int K, Q, L, B, Kn, P = 0;
	scanf("%d %d %d %d %d %d", &K, &Q, &L, &B, &Kn, &P);

	if (K != 1) {
		printf("%d ", 1 - K);
	}
	else {
		printf("0 ");
	}

	if (Q != 1) {
		printf("%d ", 1 - Q);
	}
	else {
		printf("0 ");
	}

	if (L != 2) {
		printf("%d ", 2 - L);
	}
	else {
		printf("0 ");
	}

	if (B != 2) {
		printf("%d ", 2 - B);
	}
	else {
		printf("0 ");
	}

	if (Kn != 2) {
		printf("%d ", 2 - Kn);
	}
	else {
		printf("0 ");
	}

	if (P != 8) {
		printf("%d", 8 - P);
	}
	else {
		printf("0");
	}

	return 0;
}
#endif
