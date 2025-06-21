#include <iostream>
#include <stack>
#include <cstring>
#define SZ 10000

// stack.pop �� ��ȯ���� ����.
// pop�� ���� �����ְ� �����Ÿ� top���� ����ϰ� pop���� ����

// ���� ��������� pop�ϸ� ���� �߻���. ������� ���� ��쿡�� �����ϵ��� �ϱ�
// empty�� ��������� 1, �ƴϸ� 0

// top �Լ��� ��������� ����ϸ� ����

// ���ڿ� char �迭�� ����� strcmp ��밡��. #include<cstring>
// ���ڿ��� string ������ ������ strcmp ���Ұ���. ������. #include<string>

using namespace std;

int main() {

	stack<int> stack;

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int v;
		string command;

		cin >> command;
		if (command.compare("push") == 0) {
			cin >> v;
			stack.push(v);
		}
		else if (command.compare("pop") == 0) {
			if (!stack.empty()) {
				cout << stack.top() << endl;
				stack.pop();

			}
			else {
				cout << -1 << endl;
			}
		}
		else if (command.compare("size") == 0) {
			cout << stack.size() << endl;
		}
		else if (command.compare("empty") == 0) {
			cout << stack.empty() << endl;
		}
		else if (command.compare("top") == 0) {
			if (!stack.empty()) {
				cout << stack.top() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
	}
	return 0;

}