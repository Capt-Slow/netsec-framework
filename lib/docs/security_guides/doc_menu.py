from netsec import main


class DocMenu(object):

    def doc_menu(self):
        while True:
            doc_opt = raw_input('1) Information Gathering\n'
                                '\033[1;32mYour Selection >>\033[1;m  ')

            if doc_opt == '1':
                from info_gathering.info_gathering import InfoGathering
                info_docs = InfoGathering()
                info_docs.info_gathering_menu()
            elif doc_opt == 'back':
                main()
