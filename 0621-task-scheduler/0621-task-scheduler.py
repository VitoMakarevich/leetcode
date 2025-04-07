class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
          return len(tasks)
        
      
        task_occ_dict = Counter(tasks)
        
        max_occ = max(task_occ_dict.values())
        number_of_taks_of_max_occ = sum( ( 1 for task, occ in task_occ_dict.items() if occ == max_occ ) )
        intervl_for_schedule = ( max_occ-1 )*( n+1 ) + number_of_taks_of_max_occ
        
        return max( len(tasks), intervl_for_schedule)
          