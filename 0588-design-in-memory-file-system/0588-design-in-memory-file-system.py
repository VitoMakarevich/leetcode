PATH_SEPARATOR = "/"
EMPTY_MAP = {}

class Entry:
  pass

class Directory(Entry):
  def __init__(self):
    self._entries = EMPTY_MAP
  
  def __setitem__(self, name, entry):
    if self._entries is EMPTY_MAP:
      self._entries = {}
    self._entries[name] = entry

  def __getitem__(self, name):
    return self._entries.get(name)

  @property
  def entries_names(self):
    return self._entries.keys()

class File(Entry):
  def __init__(self, content):
    self._content = content

  def add_content(self, content):
    self._content += content
  
  @property
  def content(self):
    return self._content


class FileSystem:

    def __init__(self):
        self._root = Directory()

    def ls(self, path: str) -> List[str]:
        parts = path.split(PATH_SEPARATOR)[1:]
        f = self._root
        if not (len(parts) == 1 and parts[0] == ''):
          for p in parts:
            e = f[p]
            if isinstance(e, File):
              return [p]
            f = e
        return sorted(f.entries_names)
        

    def mkdir(self, path: str) -> None:
        parts = path.split(PATH_SEPARATOR)[1:]
        f = self._root
        for p in parts:
          e = f[p]
          if not e:
            e = Directory()
            f[p] = e
          f = e

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split(PATH_SEPARATOR)[1:]
        f = self._root
        for p in parts[:-1]:
          f = f[p]
        filename = parts[len(parts) - 1]
        file = f[filename]
        if not file:
          f[filename] = File(content)
        else:
          file.add_content(content)

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split(PATH_SEPARATOR)[1:]
        f = self._root
        for p in parts:
          f = f[p]
        return f.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)