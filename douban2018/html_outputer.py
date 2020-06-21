
class HtmlOutputer(object):

    def collect_data(self, movie_data):
        if movie_data is None:
            return
        fout = open('output.html', 'a+')
        for data in movie_data:
            print
            data['name'] + '|', data['rate'] + '|', data['actor'], '\n'
            fout.write('%s,' % data['name'].encode('utf-8'))
        fout.write('%s,' % data['rate'])
        fout.write('%s\n' % data['actor'].encode('utf-8'))
        fout.close()