# 6 ����
## 06-1 ���� ����
���� �� ���� �������� ������ ��Ģ
### ������ ���� ���� �����ϱ�
### 06-2 ������ ����
ADT�� ���� �˾ƺ���
#### ������ ADT
Ǫ��, ��, ���� á���� Ȯ��, �������, ���� �ֱ� ������ Ȯ��
#### ���� �����ϱ�
```c++
#include <iostream>
#include <stack>

using namespace std;

int main()W
{
	stack<int> st;
	
	st.push(10);
	st.push(20);
	st.push(30);

	while(!st.empty())
	{
		cout << st.top() << " ";
		st.pop();
	}
	cout << endl;

	return 0;
}
```
