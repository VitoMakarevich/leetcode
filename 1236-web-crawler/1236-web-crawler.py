# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
      res = []
      self._dfs(startUrl, set(), htmlParser, self._extract_hostname(startUrl), res)
      return res
    
    def _extract_hostname(self, url):
      return re.match('^(http://[^/]+)', url).group(1)

    def _same_hostname(self, url, desired_hostname):
      return url.startswith(desired_hostname)

    def _dfs(self, url, visited, parser, hostname, res):
      if url in visited:
        return
      visited.add(url)
      if self._same_hostname(url, hostname):
        res.append(url)
        for new_url in parser.getUrls(url):
          self._dfs(new_url, visited, parser, hostname, res)

