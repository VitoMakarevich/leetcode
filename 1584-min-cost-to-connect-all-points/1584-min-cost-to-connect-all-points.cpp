class UnionFind {
public:
  UnionFind(int size): parent(size), sizes(size, 1) {
    for(int i = 0; i < size; i++) {
      parent[i] = i;
    }
  }

  int find(int node) {
    int r = parent[node];
    if (r != node)
      parent[node] = find(parent[node]);
    return r;
  }

  void unionNodes(int one, int two) {
    int oneRoot = find(one);
    int twoRoot = find(two);

    if (oneRoot != twoRoot) {
      if(sizes[twoRoot] > sizes[oneRoot]) {
        parent[oneRoot] = twoRoot;
      } else if (sizes[oneRoot] > sizes[twoRoot]) {
        parent[twoRoot] = oneRoot;
      } else {
        parent[twoRoot] = oneRoot;
        sizes[oneRoot] += 1;
      }
    }
  }

  bool isConnected(int one, int two) {
    return find(one) == find(two);
  }

private:
  std::vector<int> parent;
  std::vector<int> sizes;
};

class Solution {
public:
  int minCostConnectPoints(std::vector<std::vector<int>>& points) {
      int sum = 0;
      int n = points.size();
      std::vector<bool> visited(n, false);
      using VertexDistance = std::tuple<int, int>;
      std::priority_queue<VertexDistance, std::vector<VertexDistance>, std::greater<VertexDistance>> pq;
      pq.push(std::make_tuple(0, 0));

      while (!pq.empty()) {
          auto [distance, vertex] = pq.top();
          pq.pop();

          if (visited[vertex]) continue;
          visited[vertex] = true;

          sum += distance;

          for (int pointIdx = 0; pointIdx < n; ++pointIdx) {
              if (!visited[pointIdx]) {
                  int candidateDistance = std::abs(points[pointIdx][0] - points[vertex][0]) +
                                          std::abs(points[pointIdx][1] - points[vertex][1]);
                  pq.push(std::make_tuple(candidateDistance, pointIdx));
              }
          }
      }

      return sum;
  }
};