from netsec import main


class ParentDocMenu(object):

    def parent_doc_menu(self):
        while True:
            doc_opt = raw_input('1) Security Testing Guides\n'
                                '2) Testing Lab Walkthroughs\n'
                                '3) Cheatsheets\n'
                                '\033[1;32mYour Selection >>\033[1;m  ')

            if doc_opt == '1':
                from lib.docs.security_guides.doc_menu import DocMenu
                docm = DocMenu()
                docm.doc_menu()
            elif doc_opt == '2':
                from lib.docs.test_lab_docs.testing_lab_wt_menu import TestingLabDocMenu
                tlab = TestingLabDocMenu()
                tlab.test_lab_menu()
            elif doc_opt == '3':
                from cheatsheets.cheatsheet_menu import CheatSheetMenu
                cheat_menu = CheatSheetMenu()
                cheat_menu.cheatsheet_menu()
            elif doc_opt == 'back':
                main()

