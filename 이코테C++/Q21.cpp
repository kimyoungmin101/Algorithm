#include <iostream>
#include <queue>
#include <cstring>
#include <math.h>
using namespace std;
int n, l, r;
int cnt = 0, people = 0;
int graph[50][50];
int graph_copy[50][50];
bool visited[50][50];
int dir[4][2] = { {0,1},{1,0},{0,-1},{-1,0} };

void cal(vector<pair<int,int>> &coordinate) {
	int calPeople = people / cnt;
	for (int i = 0; i < coordinate.size(); i++) {
		graph_copy[coordinate[i].first][coordinate[i].second] = calPeople;
	}
}

vector<pair<int, int>> bfs(int x, int y) {
	queue<pair<int, int>> q;
	q.push({ x,y });
	vector<pair<int, int>> coordinate;
	visited[x][y] = true;
	while (!q.empty()) {
		int cr = q.front().first;
		int cc = q.front().second;
		q.pop();
		coordinate.push_back({ cr,cc });
		cnt++;
		people += graph[cr][cc];

		for (int i = 0; i < 4; i++) {
			int nr = cr + dir[i][0];
			int nc = cc + dir[i][1];
			if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
				int dif = abs(graph[nr][nc] - graph[cr][cc]);
				if (dif >= l && dif <= r) {
					q.push({ nr,nc });
					visited[nr][nc] = true;
				}
			}
		}

	}
	return coordinate;


}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> l >> r;
	bool isFinished = false;
	int result = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph_copy[i][j];
		}
	}
	
	while (!isFinished) {
		isFinished = true;
		//bfs첨부터 끝까지 탐색
		copy(&graph_copy[0][0], &graph_copy[0][0] + 2500, &graph[0][0]);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				//solve
				vector<pair<int, int>> coordinate(bfs(i, j));
				if (coordinate.size()>1) {
					isFinished = false;
					//cal
					cal(coordinate);

				}
				//reset
				memset(visited, false, sizeof(visited));
				cnt = 0;
				people = 0;
			}
		}

		if (!isFinished)
			result++;

	}

	cout << result;
	return 0;
}
