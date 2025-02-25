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
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
      int sum = 0;
      std::vector<bool> visited(n + 1, false);
      using VertexDistance = std::tuple<int, int>;
      std::priority_queue<VertexDistance, std::vector<VertexDistance>, std::greater<VertexDistance>> pq;
      size_t index = 1;
      for(auto v: wells) {
        pq.push(std::make_tuple(v, index));
        ++index;
      }
      std::unordered_multimap<int, tuple<int, int>> graph;
      for (auto pipe: pipes) {
        graph.insert({pipe[0], std::make_tuple(pipe[1], pipe[2])});
        graph.insert({pipe[1], std::make_tuple(pipe[0], pipe[2])});
      }

      while (!pq.empty()) {
          auto [distance, vertex] = pq.top();
          pq.pop();

          if (visited[vertex]) continue;
          visited[vertex] = true;

          sum += distance;
          // cout << "adding " << vertex << " with cost " << distance << "\n"; 

          auto range = graph.equal_range(vertex);
          for (auto it = range.first; it != range.second; ++it) {
            auto [neighbour, price] = it -> second;
            if(!visited[neighbour]) {
              pq.push(std::make_tuple(price, neighbour));
            }
          }
      }

      return sum;
    }
};