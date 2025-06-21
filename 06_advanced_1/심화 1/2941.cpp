#include <iostream>
#include <cstring>

using namespace std;

int main() {

	char word[101];
	char* cptr = word;
	int cnt = 0;

	cin >> word;

	int len = strlen(word);

	char ch[8][4] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

	for (int i = 0; i < len; i++) {
		for (int j = 0; j < 8; j++) {
			if (*cptr == ch[j][0]) {
				int flag = 1;
				for (int k = 0; k < strlen(ch[j]); k++) {
					if (*(cptr + k) != ch[j][k]) {
						flag = 0;
						break;
					}
				}
				if (flag == 1) {
					cnt++;
				}
				cnt++;
			}
		}
		cptr++;
	}

	cout << cnt;

	return 0;
}