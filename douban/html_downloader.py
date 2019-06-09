import urllib.request


class HtmlDownloader(object):

    def downlod(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()