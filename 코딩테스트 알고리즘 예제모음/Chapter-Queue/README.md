# 7. ť
## 07-1 ť�� ����
���Լ��� �Ǵ� FIFO�̶�� ��. ���ð� ���������� ť�� �����ϴ� ������ Ǫ��, ������ ������ ���̶�� ��
### ť���� �����Ͱ� �̵��ϴ� ���� ���캸��
### ť�� Ư���� Ȱ���ϴ� �о�
- �۾� ��⿭
- �̺�Ʈ ó��
### ť�� ADT
### ť �����ϱ�
```cpp
#include <iostream>
#include <queue>
using namespace std;

int main()
{
	queue<int> q;

	q.push(10);
	q.push(20);
	q.push(30);
	cout << "Front: " << q.front() << endl;

	while (!q.empty())
	{
		cout << q.front() << "�� ť���� �����߽��ϴ�. " << endl;
		q.pop();
	}
	cout << "ť�� �������? " << (q.empty() ? "Yes" : "No") << endl;

	return 0;
}
```
