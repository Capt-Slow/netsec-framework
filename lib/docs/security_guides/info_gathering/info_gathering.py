# import sys
import os
# sys.path.append('../')
# sys.path.append('../../')
# sys.path.append('{root_path}/netsec-framework/'.format(root_path=os.path.expanduser('~')))
from netsec import main
from lib.docs.security_guides.doc_menu import DocMenu


class InfoGathering(object):

    def info_gathering_menu(self):
        while True:
            print 'Information Gathering:\n'
            info_opts = raw_input('1) Web Spidering\n'
                                  '2) User-Directed Web Spidering\n'
                                  '3) Discovering Hidden Content\n'
                                  '4) Using Public Info\n'
                                  '5) Discovering Hidden Parameters\n'
                                  '6) Finding Entry Points for User Input\n'
                                  '7) Identifying Server Side Technologies\n'
                                  '8) Directory Names\n'
                                  '9) Session Tokens\n'
                                  '10) 3rd Party Components\n'
                                  '0) Back to Documents Menu\n\n\n'
                                  '\033[1;32mYour Selection >>\033[1;m  '
                                  )
            if info_opts == '1':
                self.read_doc('web_spidering.txt')
                print 'https://en.wikipedia.org/wiki/Web_crawler\n'
                break
            elif info_opts == '2':
                self.read_doc('user_dir_web_spidering.txt')
                print '\n'
                break
            elif info_opts == '0':
                docm = DocMenu()
                docm.doc_menu()
            elif info_opts == 'back':
                main()

    def read_doc(self, section):
        file_path = os.path.expanduser('~') + '/netsec-framework/lib/docs/security_guides/info_gathering/man_pages'
        with open('{file_path}/{opts}'.format(file_path=file_path, opts=section)) as data:
            for i in data:
                print i.strip('\n')

