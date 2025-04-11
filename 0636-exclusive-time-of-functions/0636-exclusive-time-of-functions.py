class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        job_ids = deque()
        output = [0] * n
        first = logs[0].split(':')
        job_ids.append(int(first[0]))
        i = 1
        prev = int(first[2])
        for v in logs[1:]:
          id, event, time = v.split(':')
          id = int(id)
          time = int(time)
          if event == 'start':
            if job_ids:
              output[job_ids[-1]] += time - prev
            prev = time
            job_ids.append(id)
          else:
            output[job_ids.pop()] += time - prev + 1
            prev = time + 1
        return output
            
