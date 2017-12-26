from netsec import main


class CheatSheetMenu(object):

    def cheatsheet_menu(self):
        while True:
            wt_opt = raw_input('1) Linux\n'
                               '2) XSS\n'
                               '3) SQL Injection\n'
                               '4) Networking\n'
                               '5) OWASP: Top 10\n\n\n'
                               '\033[1;32mYour Selection >>\033[1;m  ')
            if wt_opt == '1':
                print 'Linux..'
            elif wt_opt == '2':
                print 'XSS..'
            elif wt_opt == '3':
                print 'SQL Injection'
            elif wt_opt == '4':
                print 'Networking'
            elif wt_opt == '5':
                print 'owasp top ten..'
            elif wt_opt == 'back':
                main()
