// �迭 �����ϱ�
#include<vector>
#include<algorithm>

std::vector<int> solution(std::vector<int> arr)
{
	std::sort(arr.begin(), arr.end(), [](const auto& left, const auto& right) {
		return left > right;
		});

	arr.erase(std::unique(arr.begin(), arr.end()), arr.end()); //unique�� new end�� ��ȯ(�ڷ�� �������� ����)

	return arr;
}