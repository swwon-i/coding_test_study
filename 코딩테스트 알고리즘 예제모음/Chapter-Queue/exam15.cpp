#include <queue>

using namespace std;

int solution(int N, int K)
{
	queue<int> q;

	for (int i = 1; i <= N; ++i)
	{
		q.push(i);
	}

	while (q.size() > 1)
	{
		for (int i = 0; i < K - 1; ++i)
		{
			q.push(q.front());
			q.pop();
		}
		q.pop();
	}
	return q.front();
}