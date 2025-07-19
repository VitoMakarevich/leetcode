class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for dir_files in paths:
          directory = dir_files.split(' ')[0]
          files = dir_files.split(' ')[1:]
          for file_contents in files:
            name = file_contents.split('(')[0]
            contents = file_contents[len(name) + 1:-1]
            store[contents].append(f'{directory}/{name}')
        res = []
        for content, filenames in store.items():
          if len(filenames) > 1:
            res.append(filenames)
        return res