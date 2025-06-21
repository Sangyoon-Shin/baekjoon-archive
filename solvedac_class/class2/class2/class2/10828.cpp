#include <iostream>
#include <stack>
#include <cstring>
#define SZ 10000

// stack.pop 은 반환값이 없다.
// pop한 값을 보여주고 싶은거면 top값을 출력하고 pop연산 수행

// 스택 비어있을때 pop하면 오류 발생함. 비어있지 않은 경우에만 수행하도록 하기
// empty는 비어있으면 1, 아니면 0

// top 함수도 비어있을때 사용하면 오류

// 문자열 char 배열로 만들면 strcmp 사용가능. #include<cstring>
// 문자열을 string 변수로 받으면 strcmp 사용불가능. 오류뜸. #include<string>

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