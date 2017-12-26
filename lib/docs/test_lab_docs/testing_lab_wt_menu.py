from netsec import main


class TestingLabDocMenu(object):

    def test_lab_menu(self):
        while True:
            wt_opt = raw_input('1) Damn Vulnerable Web App\n'
                               '2) Metasploitable\n'
                               '3) NOWASP\n'
                               '4) Vulnerable Network\n\n\n'
                               '\033[1;32mYour Selection >>\033[1;m  ')
            if wt_opt == '1':
                print 'DVWA..'
            elif wt_opt == '2':
                print 'meta..'
            elif wt_opt == '3':
                print 'nowasp'
            elif wt_opt == '4':
                print 'networking'
            elif wt_opt == 'back':
                main()
