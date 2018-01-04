import sys
import os
from os.path import expanduser
import time
import subprocess, signal
import logging
import datetime
from lib.user_msg import user_msg

THIS_DIR = os.path.join(__file__, os.pardir)
LIB_PATH = os.path.abspath('lib')


def main():
    while True:
        print '''\033[1;32m
 _______          __   _________
 \      \   _____/  |_/   _____/ ____   ____
 /   |   \_/ __ \   __\_____  \_/ __ \_/ ___\/
/    |    \  ___/|  | /        \  ___/\  \___
\____|__  /\___  >__|/_______  /\___  >\___  >
        \/     \/            \/     \/     \/
___________                                                __
\_   _____/___________    _____   ______  _  _____________|  | __
 |    __) \_  __ \__  \  /     \_/ __ \ \/ \/ /  _ \_  __ \  |/ /
 |     \   |  | \// __ \|  Y Y  \  ___/\     (  <_> )  | \/    <
 \___  /   |__|  (____  /__|_|  /\___  >\/\_/ \____/|__|  |__|_ \/
     \/               \/      \/     \/                        \/\033[1;3m
     - netsec.framework@gmail.com
     - Version: 1.2
     '''
        print "\033[1;31mSome functionality requires root privelages..\033[1;m \n"
        print 'Welcome, please select from the following options:'
        value = raw_input(
                          '1) Install Dependencies\n'
                          '2) Nmap Scan\n'
                          '3) MITM Attacks\n'
                          '4) Testing Labs\n'
                          '5) Documentation\n'
                          '0) Exit\n\n\n'
                          '\033[1;32mYour Selection >>\033[1;m  ')

        if value == "q":
            print 'bye bye'
            break
        elif value == '1':
            while True:
                inopt = raw_input('1) Add/Remove Repos (Required Step)\n'
                                  '2) Install NetSec Packages\n'
                                  '3) Install Extras\n\n\n'
                                  '\033[1;32mYour Selection >>\033[1;m  ')
                if inopt == '1':
                    dep_install_repos()
                elif inopt == '2':
                    deb_install_fw_packages()
                elif inopt == '3':
                    deb_install_extras()
                elif inopt == 'back':
                    break
                elif inopt == 'home':
                    main()
        elif value == '2':
            while True:
                scan_type = raw_input('1) Discovery Scan\n'
                                      '2) Port Scan\n\n\n'
                                      '\033[1;32mYour Selection >>\033[1;m  ')
                if scan_type == '1':
                    value = raw_input('What is the ip range? (0.0.0.0/24, /16)\n'
                                      'Auto scan presumes the use of eth0 (for now).'
                                      'Type auto for autoscan\n'
                                      '\033[1;32m>>\033[1;m  ')
                    if value == 'auto':
                        while True:
                            cidr = raw_input('CIDR (Classless Inter-Domain Routing) Suffix (example: 16, 24):\n\n\n'
                                             '\033[1;32m>>\033[1;m  ')
                            print 'Your ip range: ' + get_local_ip(cidr)
                            value = get_local_ip(cidr)
                            nmap_discover(value)
                            break
                    else:
                        nmap_discover(value)
                    break
                elif scan_type == '2':
                    value = raw_input('What is the hostname/IP or IP Range?\n\n\n'
                                      '\033[1;32m>>\033[1;m  ')
                    nmap_port(value)
                else:
                    break
        elif value == '3':
            while True:
                mimopt = raw_input('1) ipv4 ip forward (Step 1)\n'
                                   '2) Configure iptables\n'
                                   '3) arpspoof start\n'
                                   '4) arpspoof stop\n'
                                   '5) sslstrip start\n'
                                   '6) sslstrip off\n'
                                   '7) ettercap\n'
                                   '8) tcpdump\n'
                                   # '9) Test Lab MIM\n'
                                   '9) stop all MITM attacks\n\n\n'
                                   '\033[1;32mYour Selection >>\033[1;m')
                if mimopt == '1':
                    ip_forward()
                elif mimopt == '2':
                    mim_iptables()
                elif mimopt == '3':
                    mim_arpspoof()
                elif mimopt == '4':
                    proc_off('arpspoof')
                elif mimopt == '5':
                    mim_sslstrip()
                elif mimopt == '6':
                    proc_off('sslstrip')
                elif mimopt == '7':
                    mim_ettercap()
                elif mimopt == '8':
                    mim_tcpdump()
                elif mimopt == '9':
                    proc_off('arpspoof')
                    proc_off('sslstrip')
                    proc_off('ettercap')
                    proc_off('tcpdump')
                elif mimopt == 'back':
                    break
        elif value == '4':
            while True:
                from lib.docker_setup import DockerConfig
                dc = DockerConfig()
                dc.docker_testlab_menu()
        elif value == '5':
            while True:
                from lib.docs.parent_menu import ParentDocMenu
                pdocm = ParentDocMenu()
                pdocm.parent_doc_menu()
        if value == '0':
            exit()


def nmap_discover(hostip):
    logging.basicConfig(level=logging.DEBUG)
    while True:
        value = raw_input('Discovery Scan Type?\n'
                          '1) List Scan (-sL)\n'
                          '2) No port scan (-sn)\n'
                          '3) No ping (-Pn)\n'
                          '4) TCP SYN Ping (-PS <port_list>)\n'
                          '5) TCP ACK Ping (-PA <port_list>)\n'
                          '6) UDP Ping (-PU <port_list>\n'
                          '7) SCTP INIT Ping (-PY <port_list>)\n'
                          '8) ICMP Ping (-PE, -PP, -PM)\n'
                          '9) IP Protocol Ping (-PO)\n'
                          '10) ARP Ping (-PR)\n'
                          '11) No ARP or ND Ping (--disable-arp-ping)\n'
                          '12) Trace path to host (--traceroute)\n'
                          '13) No DNS resolution (-n)\n'
                          '14) DNS resolution for all targets (-R)\n'
                          '15) Use system DNS resolver (--system-dns)\n'
                          '16) Servers to use for reverse DNS queries (coming soon..)\n'
                          '17) Advanced Scan\n\n\n'
                          '\033[1;32mYour Selection >>\033[1;m  ')
        if value == '1':
            print user_msg['nmap_list_scan']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -sL ' + str(hostip))
                break
            else:
                break
        elif value == '2':
            print user_msg['nmap_no_port_scan']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -sn ' + str(hostip))
                break
            else:
                break
        elif value == '3':
            print user_msg['nmap_no_ping_scan']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -Pn ' + str(hostip))
                break
            else:
                break
        elif value == '4':
            while True:
                print user_msg['nmap_tcp_syn_ping_scan']
                con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
                if con == 'y':
                    ports = raw_input('\033[1;32mWhich Ports? >> \033[1;m')
                    time.sleep(2)
                    os.system('nmap -PS' + str(ports) + ' ' + str(hostip))
                    break
                else:
                    os.system('nmap -PS ' + str(hostip))
                    break
        elif value == '5':
            while True:
                print user_msg['nmap_tcp_ack_ping']
                con = raw_input('\033[1;32mCustomize ports? (y/n) >>  \033[1;m')
                if con == 'y':
                    ports = raw_input('\033[1;32mWhich Ports? >> \033[1;m')
                    time.sleep(2)
                    os.system('nmap -PA' + str(ports) + ' ' + str(hostip))
                    break
                else:
                    os.system('nmap -PA ' + str(hostip))
                    break
        elif value == '6':
            while True:
                print user_msg['nmap_udp_ping']
                con = raw_input('\033[1;32mCustomize ports? (y/n) >>  \033[1;m')
                if con == 'y':
                    ports = raw_input('\033[1;32mWhich Ports? >> \033[1;m')
                    time.sleep(2)
                    os.system('nmap -PU' + str(ports) + ' ' + str(hostip))
                    break
                else:
                    os.system('nmap -PU ' + str(hostip))
                    break
        elif value == '7':
            while True:
                print user_msg['nmap_sctp_init_ping']
                con = raw_input('\033[1;32mCustomize ports? (y/n) >>  \033[1;m')
                if con == 'y':
                    ports = raw_input('\033[1;32mWhich Ports? >> \033[1;m')
                    time.sleep(2)
                    os.system('nmap -PY' + str(ports) + ' ' + str(hostip))
                    break
                else:
                    os.system('nmap -PY ' + str(hostip))
                    break
        elif value == '8':
            print user_msg['nmap_icmp_ping']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -PP -PE -PM ' + str(hostip))
                break
            else:
                break
        elif value == '9':
            print user_msg['nmap_ip_proto_ping']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -PO ' + str(hostip))
                break
            else:
                break
        elif value == '10':
            print user_msg['nmap_arp_ping']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -PR ' + str(hostip))
                break
            else:
                break
        elif value == '11':
            print user_msg['nmap_no_arp_or_nd_ping']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap --disable-arp-ping ' + str(hostip))
                break
            else:
                break
        elif value == '12':
            print user_msg['nmap_trace_path_to_host']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap --traceroute ' + str(hostip))
                break
            else:
                break
        elif value == '13':
            print user_msg['nmap_no_dns_resolution']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -n ' + str(hostip))
                break
            else:
                break
        elif value == '14':
            print user_msg['nmap_dns_resolution_for_all']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -R ' + str(hostip))
                break
            else:
                break
        elif value == '15':
            print user_msg['nmap_use_system_dns_resolver']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                time.sleep(2)
                os.system('nmap -R ' + str(hostip))
                break
            else:
                break
        elif value == '17':
            while True:
                print 'Add multiple flags separated by space.\n\n\n'
                flg = raw_input('Flags >>  ')
                time.sleep(2)
                run_cmmnd = 'nmap ' + str(flg) + ' ' + str(hostip)
                print 'Running the following command: ' + run_cmmnd
                os.system('nmap ' + str(flg) + ' ' + str(hostip))
                if flg == 'back':
                    break
        elif value == 'back':
            break


def get_local_ip(cidr):
    proc = subprocess.Popen(["/sbin/ifconfig | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'"],
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    ip_arr = out.split()
    ipv4_addr = ip_arr[0]
    proj_range = ipv4_addr.split('.')
    ip_range = proj_range[0] + '.' + proj_range[1] + '.' + proj_range[2] + '.0/' + cidr
    return ip_range


def get_local_gateway():
    proc = subprocess.Popen(["route -n | grep 'UG' | awk '{print $2}'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out


def get_interfaces():
    proc = subprocess.Popen(["ls /sys/class/net"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    intf_arr = out.split(' ')
    return intf_arr


def nmap_port(ip):
    while True:
        value = raw_input('Which port scan?\n'
                          '1) TCP SYN (-sS)\n'
                          '2) TCP connect (-sT)\n'
                          '3) UDP (-sU)\n'
                          '4) SCTP INIT (-sY)\n'
                          '5) TCP NULL (-sN)\n'
                          '6) FIN (-sF)\n'
                          '7) Xmas (-sX)\n'
                          '8) TCP ACK (-sA)\n'
                          '9) TCP Window (-sW)\n'
                          '10) TCP Maimon (-sM)\n'
                          '11) Custom TCP (--scanflags)\n'
                          '12) SCTP COOKIE ECHO (-sZ)\n'
                          '13) <zombie host>[:<probeport>] (idle scan) (-sI) (Coming soon..)\n'
                          '14) IP protocol (-sO)\n'
                          '15) Advanced Scan\n\n\n'
                          '\033[1;32mYour Selection >>  \033[1;m')
        if value == '1':
            print user_msg['nmap_port_tcp_syn']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sS ' + str(ip))
                break
            else:
                break
        elif value == '2':
            print user_msg['nmap_port_tcp_connect']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sT ' + str(ip))
                break
            else:
                break
        elif value == '3':
            print user_msg['nmap_port_udp']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sU ' + str(ip))
                break
            else:
                break
        elif value == '4':
            print user_msg['nmap_port_sctp_init']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sY ' + str(ip))
                break
            else:
                break
        elif value == '5':
            print user_msg['nmap_port_tcp_null']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sN ' + str(ip))
                break
            else:
                break
        elif value == '6':
            print user_msg['nmap_port_fin']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sF ' + str(ip))
                break
            else:
                break
        elif value == '7':
            print user_msg['nmap_port_xmas']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sX ' + str(ip))
                break
            else:
                break
        elif value == '8':
            print user_msg['nmap_port_tcp_ack']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sA ' + str(ip))
                break
            else:
                break
        elif value == '9':
            print user_msg['nmap_port_tcp_window']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sW ' + str(ip))
                break
            else:
                break
        elif value == '10':
            print user_msg['nmap_port_tcp_maimon']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sM ' + str(ip))
                break
            else:
                break
        elif value == '11':
            while True:
                print user_msg['nmap_port_custom_tcp']
                flgs = raw_input('What flags would you like to set? (example: URGACKPSHRSTSYNFIN sets everything\n\n\n'
                                 '\033[1;32m>>  \033[1;m')
                os.system('nmap --scanflags ' + str(flgs) + ' ' + str(ip))
                if flgs == 'back':
                    break
        elif value == '12':
            print user_msg['nmap_port_sctp_cookie_echo']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sZ ' + str(ip))
                break
            else:
                break
        elif value == '14':
            print user_msg['nmap_port_ip_protocol']
            con = raw_input('\033[1;32mContinue? (y/n) >>  \033[1;m')
            if con == 'y':
                os.system('nmap -sO ' + str(ip))
                break
            else:
                break
        elif value == 'back':
            break
        elif value == '15':
            while True:
                print 'Add multiple flags separated by space.\n\n\n'
                flg = raw_input('\033[1;32mFlags >>  \033[1;m')
                time.sleep(2)
                run_cmmnd = 'nmap ' + str(flg) + ' ' + str(ip)
                print 'Running the following command: ' + run_cmmnd
                os.system('nmap ' + str(flg) + ' ' + str(ip))
                if flg == 'back':
                    break
        elif value == 'back':
            break


def dep_install_repos():
    while True:
        iopt = raw_input('1) Add Kali Repositories\n'
                         '2) Update\n'
                         '3) Remove Kali Repositories (fixme)\n'
                         '4) View contents of source.list\n\n\n'
                         '\033[1;32mYour Selection >>\033[1;m  ')
        if iopt == '1':
            print '\033[5mAdding repos..\033[5;m'
            os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
            os.system("echo '# Kali linux repositories | Added by NetSec\n"
                      "deb http://http.kali.org/kali kali-rolling main contrib non-free\n")
        elif iopt == '2':
            os.system('apt-get update -m')
        elif iopt == '3':
            print '\033[5mRemoving repos..\033[5;m'
            infile = '/etc/apt/sources.list'
            outfile = '/etc/apt/sources.list'
            delete_list = ["# Kali linux repositories | Added by NetSec\n",
                           "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
            inf = open(infile)
            os.remove('/etc/apt/sources.list')
            outf = open(outfile, 'w+')
            for line in outf:
                for word in delete_list:
                    line = line.replace(word, '')
                outf.write(line)
            inf.close()
            outf.close()
        elif iopt == '4':
            srclst = open('/etc/apt/sources.list', 'r')
            print srclst.read()
        elif iopt == 'back':
            break
        elif iopt == 'home':
            main()


def deb_install_fw_packages():
    while True:
        sl_pckg = raw_input('Select the following package to install:\n'
                            '1) nmap\n'
                            '2) tcpdump\n'
                            '3) sslstrip\n'
                            '4) ettercap\n'
                            '5) net-tools\n'
                            '6) iptables\n'
                            '7) dsniff\n'
                            '8) Install All\n\n\n'
                            '\033[1;32mYour Selection >>\033[1;m  ')
        if sl_pckg == '1':
            os.system('apt-get -y install nmap')
        elif sl_pckg == '2':
            os.system('apt-get -y install tcpdump')
        elif sl_pckg == '3':
            os.system('apt-get -y install sslstrip')
        elif sl_pckg == '4':
            os.system('apt-get -y install ettercap-common')
        elif sl_pckg == '5':
            os.system('apt-get -y install net-tools')
        elif sl_pckg == '6':
            os.system('apt-get -y install iptables')
        elif sl_pckg == '7':
            os.system('apt-get -y install dsniff')
        elif sl_pckg == '8':
            os.system('apt-get -y install nmap sslstrip ettercap-common net-tools tcpdump iptables dsniff')
        elif sl_pckg == 'back':
            break
        elif sl_pckg == 'home':
            main()


def deb_install_extras():
    while True:
        exopt = raw_input('1) Kali Menu\n'
                          '2) Information Gathering Tools\n'
                          '3) Vulnerability Analysis\n'
                          '4) Wireless Attacks\n'
                          '5) Web Application Analysis\n'
                          '6) Sniffing & Spoofing\n'
                          '7) Maintaining Access\n'
                          '8) Reporting Tools\n'
                          '9) Exploitation Tools\n'
                          '10) Forensic Tools\n'
                          '11) Stress Testing\n'
                          '12) Password Attacks\n'
                          '13) Reverse Engineer\n'
                          '14) Hardware Hacking\n'
                          '\033[1;32mYour Selection >>\033[1;m  ')
        if exopt == '1':
            print 'Installing Kali menus..'
            os.system('apt-get install kali-menu')
        elif exopt == 'back':
            break
        elif exopt == '2':
            install_info_tools()
        elif exopt == '3':
            install_vuln_tools()
        elif exopt == '4':
            install_wifi_tools()
        elif exopt == '5':
            install_web_tools()
        elif exopt == '6':
            install_sniff_tools()
        elif exopt == '7':
            install_maint_tools()
        elif exopt == '8':
            install_rpt_tools()
        elif exopt == '9':
            install_exp_tools()
        elif exopt == '10':
            install_fore_tools()
        elif exopt == '11':
            install_stress_tools()
        elif exopt == '12':
            install_pw_tools()
        elif exopt == '13':
            install_re_tools()
        elif exopt == '14':
            install_hw_tools()
        elif exopt == 'home':
            main()


def install_info_tools():
    info_tools_arr = [
        '0) acccheck', '1) ace-voip', '2) amap', '3) automater', '4) braa', '5) casefile', '6) cdpsnarf',
        '7) cisco-torch', '8) cookie-cadger', '9) copy-router-config', '10) dmitry', '11) dnmap', '12) dnsenum',
        '13) dnsmap', '14) dnsrecon', '15) dnstracer', '16) dnswalk', '17) dotdotpwn', '18) enum4linux', '19) enumiax',
        '20) exploitdb', '21) fierce', '22) firewalk', '23) fragroute', '24) fragrouter', '25) ghost-phisher',
        '26) golismero', '27) goofile', '28) lbd', '29) maltego-teeth', '30) masscan', '31) metagoofil', '32) miranda',
        '33) ntop', '34) p0f', '35) parsero', '36) recon-ng', '37) set', '38) smtp-user-enum', '39) snmpcheck',
        '40) sslcaudit', '41) sslsplit', '42) sslyze', '43) thc-ipv6', '44) theharvester', '45) tlssled', '46) twofi',
        '47) urlcrazy', '48) wireshark', '49) wol-e', '50) xplico', '51) ismtp', '52) intrace', '53) hping3',
        '54) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the Information Gathering tools to install:\033[1;m'
        for i in info_tools_arr:
            print i
        info_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if info_tools_opt == int:
            for i in info_tools_arr:
                tx.append(i.split(' '))
            print 'Installing.. ' + tx[int(info_tools_opt)][1]
            if int(info_tools_opt) < 54:
                os.system('apt-get install -y ' + tx[int(info_tools_opt)][1])
            if info_tools_opt == '54':
                print '(please be patient)'
                for i in xrange(54):
                    os.system('apt-get install -y ' + tx[i][1])
        elif info_tools_opt == 'back':
            deb_install_extras()
        elif info_tools_opt == 'home':
            main()


def install_vuln_tools():
    vuln_tools_arr = [
        '0) bbqsql', '1) bed', '2) cisco-auditing-tool', '3) cisco-global-exploiter', '4) cisco-ocs', '5) cisco-torch',
        '6) copy-router-config', '7) doona', '8) dotdotpwn', '9) greenbone-security-assistant', '10) hexorbase',
        '11) inguma', '12) jsql', '13) lynis', '14) ohrwurm', '15) openvas-administrator', '16) openvas-cli',
        '17) openvas-manager', '18) openvas-scanner', '19) oscanner', '20) powerfuzzer', '21) sfuzz', '22) sidguesser',
        '23) siparmyknife', '24) sqlmap', '25) sqlninja', '26) sqlsus', '27) thc-ipv6', '28) tnscmd10g',
        '29) unix-privesc-check', '30) yersinia', '31) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Vulnerability Analysis tools to install:\033[1;m'
        for i in vuln_tools_arr:
            print i
        vuln_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if vuln_tools_opt == int:
            for i in vuln_tools_arr:
                tx.append(i.split(' '))
            print 'Installing.. ' + tx[int(vuln_tools_opt)][1]
            if int(vuln_tools_opt) < 31:
                os.system('apt-get install -y ' + tx[int(vuln_tools_opt)][1])
            if vuln_tools_opt == '31':
                print '(please be patient)'
                for i in xrange(31):
                    os.system('apt-get install -y ' + tx[i][1])
        elif vuln_tools_opt == 'back':
            deb_install_extras()
        elif vuln_tools_opt == 'home':
            main()


def install_wifi_tools():
    wifi_tools_arr = [
        '0) aircrack-ng', '1) asleap', '2) bluelog', '3) blueranger', '4) bluesnarfer', '5) bully', '6) cowpatty',
        '7) crackle', '8) eapmd5pass', '9) fern-wifi-cracker', '10) ghost-phisher', '11) giskismet', '12) gqrx',
        '13) kalibrate-rtl', '14) killerbee', '15) kismet', '16) mdk3', '17) mfcuk', '18) mfoc', '19) mfterm',
        '20) multimon-ng', '21) pixiewps', '22) reaver', '23) redfang', '24) rtlsdr-scanner', '25) spooftooph',
        '26) wifi-honey', '27) wifitap', '28) wifite', '29) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Wifi Attack tools to install:\033[1;m'
        for i in wifi_tools_arr:
            print i
        wifi_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if wifi_tools_opt == int:
            for i in wifi_tools_arr:
                tx.append(i.split(' '))
            if int(wifi_tools_opt) < 29:
                print 'Installing.. ' + tx[int(wifi_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(wifi_tools_opt)][1])
            if wifi_tools_opt == '29':
                print '(please be patient)'
                for i in xrange(29):
                    os.system('apt-get install -y ' + tx[i][1])
        elif wifi_tools_opt == 'back':
            deb_install_extras()
        elif wifi_tools_opt == 'home':
            main()


def install_web_tools():
    web_tools_arr = [
        '0) apache-users', '1) arachni', '2) bbqsql', '3) blindelephant', '4) burpsuite', '5) cutycapt', '6) davtest',
        '7) deblaze', '8) dirb', '9) dirbuster', '10) fimap', '11) funkload', '12) grabber', '13) jboss-autopwn',
        '14) joomscan', '15) jsql', '16) maltego-teeth', '17) padbuster', '18) paros', '19) parsero', '20) plecost',
        '21) powerfuzzer', '22) proxystrike', '23) recon-ng', '24) skipfish', '25) sqlmap', '26) sqlninja',
        '27) sqlsus', '28) ua-tester', '29) uniscan', '30) vega', '31) w3af', '32) webscarab', '33) webshag',
        '34) websploit', '35) wfuzz', '36) wpscan', '37) xsser', '38) zaproxy', '39) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Web Applications tools to install:\033[1;m'
        for i in web_tools_arr:
            print i
        web_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if web_tools_opt == int:
            for i in web_tools_arr:
                tx.append(i.split(' '))
            if int(web_tools_opt) < 39:
                print 'Installing.. ' + tx[int(web_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(web_tools_opt)][1])
            if web_tools_opt == '39':
                print '(please be patient)'
                for i in xrange(39):
                    os.system('apt-get install -y ' + tx[i][1])
        elif web_tools_opt == 'back':
            deb_install_extras()
        elif web_tools_opt == 'home':
            main()


def install_sniff_tools():
    sniff_tools_arr = [
        '0) dnschef', '1) fiked', '2) hamster-sidejack', '3) hexinject', '4) iaxflood', '5) inviteflood', '6) ismtp',
        '7) mitmproxy', '8) ohrwurm', '9) protos-sip', '10) rebind', '11) responder', '12) rtpbreak',
        '13) rtpinsertsound', '14) rtpmixsound', '15) sctpscan', '16) siparmyknife', '17) sipp', '18) sipvicious',
        '19) sniffjoke', '20) sslsplit', '21) voiphopper', '22) webscarab', '23) wireshark', '24) wifi-honey',
        '25) xspy', '26) yersinia', '27) zaproxy', '28) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Web Applications tools to install:\033[1;m'
        for i in sniff_tools_arr:
            print i
        sniff_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if sniff_tools_opt == int:
            for i in sniff_tools_arr:
                tx.append(i.split(' '))
            if int(sniff_tools_opt) < 28:
                print 'Installing.. ' + tx[int(sniff_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(sniff_tools_opt)][1])
            if sniff_tools_opt == '28':
                print '(please be patient)'
                for i in xrange(28):
                    os.system('apt-get install -y ' + tx[i][1])
        elif sniff_tools_opt == 'back':
            deb_install_extras()
        elif sniff_tools_opt == 'home':
            main()


def install_maint_tools():
    maint_tools_arr = [
        '0) cryptcat', '1) cymothoa', '2) dbd', '3) dns2tcp', '4) http-tunnel', '5) httptunnel', '6) intersect',
        '7) nishang', '9) polenum', '10) powersploit', '11) pwnat', '12) ridenum', '13) sbd', '14) u3-pwn',
        '15) webshells', '16) weevely', '17) winexe', '18) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Maintaining Access tools to install:\033[1;m'
        for i in maint_tools_arr:
            print i
        maint_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if maint_tools_opt == int:
            for i in maint_tools_arr:
                tx.append(i.split(' '))
            if int(maint_tools_opt) < 18:
                print 'Installing.. ' + tx[int(maint_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(maint_tools_opt)][1])
            if maint_tools_opt == '18':
                print '(please be patient)'
                for i in xrange(18):
                    os.system('apt-get install -y ' + tx[i][1])
        elif maint_tools_opt == 'back':
            deb_install_extras()
        elif maint_tools_opt == 'home':
            main()


def install_rpt_tools():
    rpt_tools_arr = [
        '0) casefile', '1) cutycapt', '2) dos2unix', '3) dradis', '4) keepnote', '5) magictree', '6) metagoofil',
        '7) nipper-ng', '8) pipal', '9) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Reporting tools to install:\033[1;m'
        for i in rpt_tools_arr:
            print i
        rpt_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if rpt_tools_opt == int:
            for i in rpt_tools_arr:
                tx.append(i.split(' '))
            if int(rpt_tools_opt) < 9:
                print 'Installing.. ' + tx[int(rpt_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(rpt_tools_opt)][1])
            if rpt_tools_opt == '9':
                print '(please be patient)'
                for i in xrange(9):
                    os.system('apt-get install -y ' + tx[i][1])
        elif rpt_tools_opt == 'back':
            deb_install_extras()
        elif rpt_tools_opt == 'home':
            main()


def install_exp_tools():
    exp_tools_arr = [
        '0) armitage', '1) backdoor-factory', '2) beef-xss', '3) cisco-auditing-tool', '4) cisco-global-exploiter',
        '5) cisco-ocs', '6) cisco-torch', '7) crackle', '8) jboss-autopwn', '9) linux-exploit-suggester',
        '10) maltego-teeth', '11) set', '12) shellnoob', '13) sqlmap', '14) thc-ipv6', '15) yersinia', '16) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Exploiting tools to install:\033[1;m'
        for i in exp_tools_arr:
            print i
        exp_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if exp_tools_opt == int:
            for i in exp_tools_arr:
                tx.append(i.split(' '))
            if int(exp_tools_opt) < 16:
                print 'Installing.. ' + tx[int(exp_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(exp_tools_opt)][1])
            if exp_tools_opt == '16':
                print '(please be patient)'
                for i in xrange(16):
                    os.system('apt-get install -y ' + tx[i][1])
        elif exp_tools_opt == 'back':
            deb_install_extras()
        elif exp_tools_opt == 'home':
            main()


def install_fore_tools():
    fore_tools_arr = [
        '0) binwalk', '1) bulk-extractor', '2) chntpw', '3) cuckoo', '4) dc3dd', '5) ddrescue', '6) dff',
        '7) dumpzilla', '8) extundelete', '9) foremost', '10) galleta', '11) guymager', '12) iphone-backup-analyzer',
        '13) p0f', '14) pdf-parser', '15) pdfid', '16) pdgmail', '17) peepdf', '18) regripper', '19) volatility',
        '20) xplico', '21) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Forensic tools to install:\033[1;m'
        for i in fore_tools_arr:
            print i
        fore_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if fore_tools_opt == int:
            for i in fore_tools_arr:
                tx.append(i.split(' '))
            if int(fore_tools_opt) < 21:
                print 'Installing.. ' + tx[int(fore_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(fore_tools_opt)][1])
            if fore_tools_opt == '21':
                print '(please be patient)'
                for i in xrange(21):
                    os.system('apt-get install -y ' + tx[i][1])
        elif fore_tools_opt == 'back':
            deb_install_extras()
        elif fore_tools_opt == 'home':
            main()


def install_stress_tools():
    stress_tools_arr = [
        '0) dhcpig', '1) funkload', '2) iaxflood', '3) inviteflood', '4) ipv6-toolkit', '5) mdk3', '6) reaver',
        '7) rtpflood', '8) slowhttptest', '9) t50', '10) thc-ipv6', '11) thc-ssl-dos', '12) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Stress Testing tools to install:\033[1;m'
        for i in stress_tools_arr:
            print i
        stress_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if stress_tools_opt == int:
            for i in stress_tools_arr:
                tx.append(i.split(' '))
            if int(stress_tools_opt) < 12:
                print 'Installing.. ' + tx[int(stress_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(stress_tools_opt)][1])
            if stress_tools_opt == '12':
                print '(please be patient)'
                for i in xrange(12):
                    os.system('apt-get install -y ' + tx[i][1])
        elif stress_tools_opt == 'back':
            deb_install_extras()
        elif stress_tools_opt == 'home':
            main()


def install_pw_tools():
    pw_tools_arr = [
        '0) acccheck', '1) burpsuite', '3) cewl', '4) chntpw', '5) cisco-auditing-tool', '6) cmospwd', '7) creddump',
        '8) crunch', '9) findmyhash', '10) gpp-decrypt', '11) hash-identifier', '12) hexorbase', '13) john',
        '14) johnny', '15) keimpx', '16) maltego-teeth', '17) maskprocessor', '18) multiforcer', '19) ncrack',
        '20) oclgausscrack', '21) pack', '22) patator', '23) polenum', '24) rainbowcrack', '25) rcracki-mt',
        '26) rsmangler', '27) sqldict', '28) statsprocessor', '29) thc-pptp-bruter', '30) truecrack', '31) webscarab',
        '32) wordlists', '33) zaproxy', '34) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Password Attack tools to install:\033[1;m'
        for i in pw_tools_arr:
            print i
        pw_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if pw_tools_opt == int:
            for i in pw_tools_arr:
                tx.append(i.split(' '))
            if int(pw_tools_opt) < 34:
                print 'Installing.. ' + tx[int(pw_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(pw_tools_opt)][1])
            if pw_tools_opt == '34':
                print '(please be patient)'
                for i in xrange(34):
                    os.system('apt-get install -y ' + tx[i][1])
        elif pw_tools_opt == 'back':
            deb_install_extras()
        elif pw_tools_opt == 'home':
            main()


def install_re_tools():
    re_tools_arr = [
        '0) apktool', '1) dex2jar', '2) python-diStorm3', '3) edb-debugger', '4) jad', '5) javasnoop', '6) JD',
        '7) OllyDbg', '8) smali', '9) Valgrind', '10) YARA', '11) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Reverse Engineering tools to install:\033[1;m'
        for i in re_tools_arr:
            print i
        re_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if re_tools_opt == int:
            for i in re_tools_arr:
                tx.append(i.split(' '))
            if int(re_tools_opt) < 11:
                print 'Installing.. ' + tx[int(re_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(re_tools_opt)][1])
            if re_tools_opt == '11':
                print '(please be patient)'
                for i in xrange(11):
                    os.system('apt-get install -y ' + tx[i][1])
        elif re_tools_opt == 'back':
            deb_install_extras()
        elif re_tools_opt == 'home':
            main()


def install_hw_tools():
    hw_tools_arr = [
        '0) android-sdk', '1) apktool', '2) arduino', '3) dex2jar', '4) sakis3g', '5) smali', '6) All tools'
    ]
    while True:
        print '\033[1;32mSelect one of the following Hardware Hacking tools to install:\033[1;m'
        for i in hw_tools_arr:
            print i
        hw_tools_opt = raw_input('\033[1;32mYour Selection >>\033[1;m  ')
        tx = []
        if hw_tools_opt == int:
            for i in hw_tools_arr:
                tx.append(i.split(' '))
            if int(hw_tools_opt) < 11:
                print 'Installing.. ' + tx[int(hw_tools_opt)][1]
                os.system('apt-get install -y ' + tx[int(hw_tools_opt)][1])
            if hw_tools_opt == '11':
                print '(please be patient)'
                for i in xrange(11):
                    os.system('apt-get install -y ' + tx[i][1])
        elif hw_tools_opt == 'back':
            deb_install_extras()
        elif hw_tools_opt == 'home':
            main()


def ip_forward():
    while True:
        on_off = raw_input('Toggle IP Forwarding:\n'
                           '1) on\n'
                           '2) off\n'
                           '3) check current status\n\n\n'
                           '\033[1;32mYour Selection >>\033[1;m  ')
        if on_off == '1':
            print 'Turning on..'
            os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
        elif on_off == '2':
            print 'Turning off..'
            os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')
        elif on_off == '3':
            ipfw = open('/proc/sys/net/ipv4/ip_forward', 'r')
            print ipfw.read()
        elif on_off == 'back':
            break
        elif on_off == 'home':
            main()


def mim_iptables():
    while True:
        table_tgl = raw_input('iptables:\n'
                              '1) set\n'
                              '2) view current rules\n\n\n'
                              '\033[1;32mYour Selection >>\033[1;m')
        if table_tgl == '1':
            print 'default listening port 777'
            print 'press Enter for default\n'
            prtf = raw_input('\033[1;32mWhich port? >>\033[1;m ')
            if prtf == 'back':
                break
            elif prtf == '':
                os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 777')
                print 'set: iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 777'
            else:
                print 'setting: iptables -t nat -A PREROUTING -p tcp ' \
                      '--destination-port 80 -j REDIRECT --to-port ' + str(prtf)

                os.system('iptables -t nat -A PREROUTING -p tcp '
                          '--destination-port 80 -j REDIRECT --to-port ' + str(prtf))
                break
        elif table_tgl == '2':
            os.system('iptables -L')
        elif table_tgl == 'back':
            break
        elif table_tgl == 'home':
            main()


def mim_arpspoof():
    while True:
        print 'Your Interfaces:'
        for i in get_interfaces():
            print i
        print 'Which on to use?'
        print 'Your Gateway:'
        print get_local_gateway()
        print 'Enter your interface, target IP and gateway (Example: eth0 192.168.1.3 192.168.1.1)'
        arpopt = raw_input('\033[1;32m >>\033[1;m')
        arpopt_arr = arpopt.split(' ')
        print 'arpspoof is now running...'
        try:
            cmd = 'arpspoof -i ' + str(arpopt_arr[0]) + ' -t ' + str(arpopt_arr[1]) + ' ' + str(arpopt_arr[2] + ' &')
            print str(cmd)
            os.system(cmd)
            break
        except IndexError:
            print '\033[1;31mOops! Invalid Input\033[1;m'

        break


def proc_off(proc):
    print 'Turning off ' + str(proc) + '..'
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    (out, err) = p.communicate()
    for line in out.splitlines():
        if proc in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


def mim_sslstrip():
    while True:
        print 'Look in current dir for sslstrip.log file'
        print '\033[1;31mport used should be same as iptables port\033[1;m\n'
        portopt = raw_input('Default port 777. (Press Enter for default)\n'
                            '\033[1;32mlisten port >>\033[1;m')
        if portopt == '':
            print 'Launching sslstrip...'
            os.system('sslstrip -l 777 &')
            break
        elif portopt == 'back':
            break
        else:
            print 'Listening on port ' + str(portopt) + '...'
            os.system('sslstrip -l ' + str(portopt) + ' &')


def mim_ettercap():
    ptime = datetime.datetime.now()
    while True:
        print 'A pcap file will be created in your home directory.\n'
        ett_opt = raw_input('1) Poison Gateway\n'
                            '2) Poison IP\n'
                            '3) Stop Ettercap\n'
                            '\033[1;32mYour Selection >>\033[1;m')
        if ett_opt == '1':
            print '\033[1;31mRunning the following command: \033[1;m'
            print 'ettercap -T -q -M ARP /{0}/// -w {1}/{2}.pcap >/dev/null 2>&1 &'\
                .format(get_local_gateway(), expanduser('~'), ptime.strftime("%s"))
            print '-T (text only GUI)'
            print '-q (quiet mode - packet verbosity off)'
            print '-M (method)'
            print '/// (collect entire IP range)'
            print '-w (write to pcap file)\n'
            print 'Poisoning Gateway...'
            os.system('ettercap -T -q -M ARP /{0}/// -w {1}/{2}.pcap >/dev/null 2>&1 &'
                      .format(get_local_gateway(), expanduser('~'), ptime.strftime("%s")))

        elif ett_opt == '2':
            while True:
                ett_ip = raw_input('\033[1;32mEnter the IP:\033[1;m')
                break
            print 'Poisoning {0}'.format(ett_ip)
            print '\033[1;31mRunning the following command: \033[1;m'
            print 'ettercap -T -q -M ARP /{0}/// -w {1}/{2}.pcap >/dev/null 2>&1 &'\
                .format(ett_ip, expanduser('~'), ptime.strftime("%s"))
            os.system('ettercap -T -q -M ARP /{0}/// -w {1}/{2}.pcap >/dev/null 2>&1 &'
                      .format(ett_ip, expanduser('~'), ptime.strftime("%s")))
        elif ett_opt == '3':
            print 'Turning off ettercap..'
            proc_off('ettercap')
        elif ett_opt == 'back':
            break
        elif ett_opt == 'home':
            main()


def mim_tcpdump():
    while True:
        t = datetime.datetime.now()
        print 'Select one of the following interface to listen:\n'
        for i in get_interfaces():
            print i
        tcp_face = raw_input('\033[1;32mYour Selection >> \033[1;m')
        if tcp_face == 'back':
            break
        else:
            cmd = 'tcpdump -ni {0} -w {1}/{2}.pcap >/dev/null 2>&1 &'\
                .format(tcp_face, expanduser('~'), t.strftime("%s"))
            print '\033[1;31mRunning the following command: \033[1;m'
            print cmd
            print '-i (interface)'
            print "-n (don't convert addresses to names)"
            print '-w (write pcap file)'
            print 'sniffing...\n'
            print 'This will create a pcap file in your home dir.'
            os.system(cmd)


if __name__ == "__main__":
    main()
