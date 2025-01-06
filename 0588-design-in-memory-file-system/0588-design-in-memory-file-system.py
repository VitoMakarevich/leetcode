class Entry:
  def __init__(self, is_dir):
    self._is_dir = is_dir
    self._entries = {}
    self._content = ""
  def add_content(self, content):
    if self._content == "":
      self._content = content
    else:
      self._content += content

class FileSystem:

    def __init__(self):
        self.root = Entry(True)

    def ls(self, path: str) -> List[str]:
        parts = path.split('/')[1:]
        f = self.root
        if not (len(parts) == 1 and parts[0] == ''):
          for p in parts:
            f = f._entries[p]
        return sorted(f._entries.keys())
        

    def mkdir(self, path: str) -> None:
        parts = path.split('/')[1:]
        f = self.root
        for p in parts:
          if not p in f._entries:
            f._entries[p] = Entry(True)
          f = f._entries[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split('/')[1:]
        f = self.root
        for p in parts[:-1]:
          f = f._entries[p]
        filename = parts[len(parts) - 1]
        if filename not in f._entries:
          f._entries[filename] = Entry(False)
        f._entries[filename].add_content(content)

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split('/')[1:]
        f = self.root
        for p in parts:
          f = f._entries[p]
        return f._content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)