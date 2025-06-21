#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string s1, string s2) {
	return s1 < s2;
}

int main() {

	string s[20000];

	int n;
	int idx = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int j = i;
		string tmp;
		cin >> tmp;
		while (j > 0) {
			if (s[i] == tmp) {
				j = -1;
			}
			j--;
		}
		if (j != -1) {
			s[i] = tmp;
			idx++;
		}

	}

	sort(s, s + idx, compare);

	for (int i = 0; i < idx; i++) {
		cout << s[i] << endl;
	}

	return 0;
}