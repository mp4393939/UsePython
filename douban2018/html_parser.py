from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self):
        pass

    def parser_html(self, cnt):
        if cnt is None:
            return
        soup = BeautifulSoup(cnt, 'html.parser', from_encoding='utf-8')
        # movie_name, movie_desc, movie_rate =
        return self.get_movie_names(soup)

    def get_movie_names(self, soup):
        movie_data = []
        movie_all = soup.find('div', class_='article').find_next('table').find_next_sibling('div').find_next_sibling(
            'div').find_all('table')
        count = 1
        for movie_one in movie_all:
            movie_data.append(self.get_movie_name(movie_one))
            # if count > 2:
            #   break
            count += 1
        return movie_data

    def get_movie_name(self, cnt):
        info = {}
        soup = BeautifulSoup(str(cnt), 'html.parser', from_encoding='utf-8')
        movie_one = soup.find('tr', class_='item').find_next('td').find_next_sibling('td').find('div', class_='pl2')
        info['name'] = movie_one.find('a').get_text().replace("\n", "").replace(" ", "")
        info['actor'] = movie_one.find('p', class_='pl').get_text().replace("\n", "").replace(" ", "")
        info['rate'] = movie_one.find('div', class_='star clearfix').find('span', class_='rating_nums').get_text()
        return info