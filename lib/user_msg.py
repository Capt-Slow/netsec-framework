user_msg = {
    'nmap_list_scan': 'The list scan is a degenerate form of host discovery that simply lists each '
                      'host of the network(s)\n specified, without sending any packets to the target hosts.\n',
    'nmap_no_port_scan': 'This option tells Nmap not to do a port scan after host discovery, and only print '
                         'out the available\n hosts that responded to the host discovery probes.\n',
    'nmap_no_ping_scan': 'This option skips the Nmap discovery stage altogether. Normally, Nmap uses this '
                         'stage to determine\n active machines for heavier scanning.',
    'nmap_tcp_syn_ping_scan': 'This option sends an empty TCP packet with the SYN flag set. The default '
                              'destination port is 80\n Alternate ports can be specified as a parameter.',
    'nmap_tcp_ack_ping': 'The TCP ACK ping is quite similar to the SYN ping. The difference, as you could\n'
                      'likely guess, is that the TCP ACK flag is set instead of the SYN flag. Such an ACK packet\n'
                      'purports to be acknowledging data over an established TCP connection, but no such connection\n'
                      'exists. So remote hosts should always respond with a RST packet, disclosing their existence in\n'
                      'the process.',
    'nmap_udp_ping': 'Another host discovery option is the UDP ping, which sends a UDP packet to the given ports.\n'
                      'For most ports, the packet will be empty, though some use a protocol-specific payload that is\n'
                      'more likely to elicit a response. Upon hitting a closed port on the target machine, '
                     'the UDP probe\n should elicit an ICMP port unreachable packet in return. This signifies to '
                     'Nmap that the machine\nis up and available.',
    'nmap_sctp_init_ping': 'This option sends an SCTP packet containing a minimal INIT chunk. The INIT chunk '
                           'suggests to the\n remote system that you are attempting to establish an association. '
                           'Normally the destination port\n will be closed, and an ABORT chunk will be sent back. '
                           'If the port happens to be open, the target\nwill take the second step of an SCTP '
                           'four-way-handshake by responding with an INIT-ACK chunk.\nIf the machine running Nmap '
                           'has a functional SCTP stack, then it tears down the nascent\nassociation by responding '
                           'with an ABORT chunk rather than sending a COOKIE-ECHO chunk which would\nbe the next '
                           'step in the four-way-handshake.',
    'nmap_icmp_ping': 'In addition to the unusual TCP, UDP and SCTP host discovery types, Nmap \n \
                  can send the standard packets sent by the ubiquitous ping program. Nmap sends an ICMP type 8\n \
                  (echo request) packet to the target IP addresses, expecting a type 0 (echo reply) in return\n \
                  from available hosts.',
    'nmap_ip_proto_ping': 'One of the newer host discovery options is the IP protocol ping, which sends IP '
                          'packets with\nthe specified protocol number set in their IP header. The protocol list '
                          'takes the same format as do\nport lists in the previously discussed TCP, UDP and SCTP '
                          'host discovery options.',
    'nmap_arp_ping': "ARP scan puts Nmap and its optimized algorithms in charge of ARP requests. And if it gets a\n \
                   response back, Nmap doesn't even need to worry about the IP-based ping packets since it already\n \
                   knows the host is up. This makes ARP scan much faster and more reliable than IP-based scans.",
    'nmap_no_arp_or_nd_ping': 'The default behavior is normally faster, but this option is useful on networks '
                              'using proxy ARP,\n in which a router speculatively replies to all ARP requests, '
                              'making every target appear to be up\n according to ARP scan.',
    'nmap_trace_path_to_host': 'Traceroutes are performed post-scan using information from the scan results to '
                               'determine the port\n and protocol most likely to reach the target.',
    'nmap_no_dns_resolution': "Tells Nmap to never do reverse DNS resolution on the active IP addresses it finds. "
                              "Since DNS can be\n slow even with Nmap's built-in parallel stub resolver, this option "
                              "can slash scanning times.",
    'nmap_dns_resolution_for_all': 'Tells Nmap to always do reverse DNS resolution on the target IP addresses. '
                                   'Normally reverse DNS\nis only performed against responsive (online) hosts.',
    'nmap_use_system_dns_resolver': 'By default, Nmap resolves IP addresses by sending queries directly to the name '
                                    'servers configured\n on your host and then listening for responses. '
                                    'Many requests (often dozens) are performed in \n parallel to improve performance. '
                                    'Specify this option to use your system resolver instead.',
    'nmap_port_tcp_syn': 'SYN scan is the default and most popular scan option for good reasons. It can be performed '
                         'quickly,\n scanning thousands of ports per second on a fast network not hampered by '
                         'restrictive firewalls. ',
    'nmap_port_tcp_connect': 'TCP connect scan is the default TCP scan type when SYN scan is not an option. '
                             'This is the case when\n a user does not have raw packet privileges.',
    'nmap_port_udp': 'While most popular services on the Internet run over the TCP protocol, UDP services are widely\n'
                     ' deployed. DNS, SNMP, and DHCP (registered ports 53, 161/162, and 67/68) are three of the most\n'
                     ' common. Because UDP scanning is generally slower and more difficult than TCP, some security\n'
                     ' auditors ignore these ports',
    'nmap_port_sctp_init': 'SCTP is a relatively new alternative to the TCP and UDP protocols, combining most '
                          'characteristics\n  of TCP and UDP, and also adding new features like multi-homing and '
                          'multi-streaming. It is mostly\n being used for SS7/SIGTRAN related services',
    'nmap_port_tcp_null': 'TCP NULL scan type exploits a subtle loophole in the TCP RFC to differentiate between '
                          'open and\n closed ports. ',
    'nmap_port_fin': 'FIN scan type exploits a subtle loophole in the TCP RFC to differentiate between open and\n'
                     ' closed ports. ',
    'nmap_port_xmas': 'Xmas scan type exploits a subtle loophole in the TCP RFC to differentiate between open and\n'
                      ' closed ports. ',
    'nmap_port_tcp_ack': 'TCP ACK scan never determines open (or even open|filtered) ports. It is used to map out '
                         'firewall\n rulesets, determining whether they are stateful or not and which ports are '
                         'filtered.',
    'nmap_port_tcp_window': 'Window scan is exactly the same as ACK scan except that it exploits an implementation '
                            'detail of\n  certain systems to differentiate open ports from closed ones, rather than '
                            'always printing\n unfiltered when a RST is returned. It does this by examining the '
                            'TCP Window field of the RST\n packets returned. On some systems, open ports use a '
                            'positive window size (even for RST packets)\n while closed ones have a zero window. '
                            'So instead of always listing a port as unfiltered when it\n receives a RST back, Window '
                            'scan lists the port as open or closed if the TCP Window value in that\n' +
                            "reset is positive or zero, respectively. This scan relies on an implementation "
                            "detail of a\n minority of systems out on the Internet, so you can't always trust it.",
    'nmap_port_tcp_maimon': 'TCP Maimon scan is exactly the same as NULL, FIN, and Xmas scans, except that the '
                            'probe is FIN/ACK.',
    'nmap_port_custom_tcp': 'Truly advanced Nmap users need not limit themselves to the canned scan types offered.',
    'nmap_port_sctp_cookie_echo': "SCTP COOKIE ECHO scan is a more advanced SCTP scan. It takes advantage of the "
                                  "fact that SCTP\n implementations should silently drop packets containing "
                                  "COOKIE ECHO chunks on open ports, but \n send an ABORT if the port is closed. "
                                  "The advantage of this scan type is that it is not as obvious \n a port scan than "
                                  "an INIT scan. Also, there may be non-stateful firewall rulesets blocking INIT \n"
                                  "chunks, but not COOKIE ECHO chunks. Don't be fooled into thinking that this will "
                                  "make a port scan \n invisible; a good IDS will be able to detect SCTP COOKIE "
                                  "ECHO scans too. The downside is that SCTP \n COOKIE ECHO scans cannot differentiate "
                                  "between open and filtered ports, leaving you with the state \n open|filtered in "
                                  "both cases.",
    'nmap_port_zombie_host': '',
    'nmap_port_ip_protocol': "IP protocol scan allows you to determine which IP protocols (TCP, ICMP, IGMP, etc.) "
                             "are supported\n by target machines. This isn't technically a port scan, since it cycles "
                             "through IP protocol \n numbers rather than TCP or UDP port numbers.",
    'nmap_port_advanced_scan': ''
}