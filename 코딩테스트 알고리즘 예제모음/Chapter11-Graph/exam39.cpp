#include <limits>   // ������ �ִ��� �ٷ�� ���̺귯��
#include <tuple>    // Ʃ���� �ٷ�� ���̺귯��
#include <vector>   // ���͸� �ٷ�� ���̺귯��

using namespace std;

// ���Ѵ� �� ���� (�ʹ� ū ���ڸ� �ǹ�)
const int INF = numeric_limits<int>::max();

// solution �Լ�: �ִ� ��θ� ���ϴ� �Լ�
vector<int> solution(int num_vertices, vector<tuple<int, int, int>> edges, int source)
{
    // �׷����� 2���� ���ͷ� ����� (�� ������ ����� �ٸ� ������� ����ġ ����)
    vector<vector<pair<int, int>>> graph(num_vertices);

    // edges�� �־��� ������ �������� �׷��� �����
    for (auto& edge : edges)
    {
        int from, to, weight;
        tie(from, to, weight) = edge;  // edge���� from, to, weight ���� �̾Ƽ� ���
        graph[from].emplace_back(to, weight);  // 'from' �������� 'to' �������� ���� ����ġ 'weight'�� ����
    }

    // �� ���������� �ִ� �Ÿ� ���� ������ ���� (ó������ ��� ���Ѵ�(INF)�� ����)
    vector<int> distance(num_vertices, INF);
    distance[source] = 0;  // ��� ������ �Ÿ��� 0

    // ����-���� �˰��� �ٽ�: ��� ������ 'num_vertices - 1'���� Ȯ���ϸ� �Ÿ� ����
    for (int i = 0; i < num_vertices - 1; ++i)
    {
        for (int u = 0; u < num_vertices; ++u)  // u: ��� ����
        {
            for (const auto& [v, weight] : graph[u])  // v: ���� ����, weight: ������ ����ġ
            {
                // ��� ���� u�� ���ļ� ���� ���� v�� ���� �Ÿ� ���
                if (distance[u] + weight < distance[v])
                {
                    distance[v] = distance[u] + weight;  // �ִ� �Ÿ� ����
                }
            }
        }
    }

    // ���� ����Ŭ�� �ִ��� Ȯ���ϱ�
    for (int u = 0; u < num_vertices; ++u)
    {
        for (const auto& [v, weight] : graph[u])
        {
            if (distance[u] + weight < distance[v])  // �Ÿ� ������ �����ϸ� ���� ����Ŭ�� �ִٴ� �ǹ�
            {
                return vector<int>(1, -1);  // ���� ����Ŭ�� ������ -1�� ��ȯ
            }
        }
    }

    return distance;  // �ִ� �Ÿ� �迭 ��ȯ
}
