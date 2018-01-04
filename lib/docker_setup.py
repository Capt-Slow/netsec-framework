import sys
import os
sys.path.append('../')
sys.path.append('../docs')
sys.path.append('{root_path}/netsec-framework/netsec.py'.format(root_path=os.path.expanduser('~')))

import subprocess
from netsec import main


class DockerConfig(object):

    def docker_testlab_menu(self):
        while True:
            docker_opt = raw_input('1) Install Docker\n'
                                   '2) Damn Vulnerable Web App\n'
                                   '3) Metasploitable\n'
                                   '4) NOWASP\n'
                                   '5) Vulnerable Network\n'
                                   '6) Kali Docker Image\n\n\n'
                                   '\033[1;32mYour Selection >>\033[1;m')
            if docker_opt == '1':
                self.auto_install_docker()
            elif docker_opt == '2':
                vuln_stack1_opts = raw_input('1) Pull & Start Docker Container\n'
                                             '2) Stop Container\n\n\n'
                                             '\033[1;32mYour Selection >>\033[1;m')
                if vuln_stack1_opts == '1':
                    self.docker_pull_and_run_images('dvwa')
                elif vuln_stack1_opts == '2':
                    self.docker_shutdown_container('dvwa')
                elif vuln_stack1_opts == 'back':
                    break
            elif docker_opt == '3':
                vuln_stack2_opts = raw_input('1) Pull & Start Docker Container\n'
                                             '2) Stop Container\n\n\n'
                                             '\033[1;32mYour Selection >>\033[1;m')
                if vuln_stack2_opts == '1':
                    self.docker_pull_and_run_images('meta')
                elif vuln_stack2_opts == '2':
                    self.docker_shutdown_container('meta')
                    break
            elif docker_opt == '4':
                vuln_stack2_opts = raw_input('1) Pull & Start Docker Container\n'
                                             '2) Stop Container\n\n\n'
                                             '\033[1;32mYour Selection >>\033[1;m')
                if vuln_stack2_opts == '1':
                    self.docker_pull_and_run_images('nowasp')
                elif vuln_stack2_opts == '2':
                    self.docker_shutdown_container('nowasp')
                    break
            elif docker_opt == '5':
                print 'This launches DVWA and a Debian container.\n' \
                      'The Debian container will continuously attempt requests to login to DVWA. \n' \
                      'This provides a contained lab to practice/execute ' \
                      'MIM credential harvesting attacks.\n'
                vuln_net_opts = raw_input('1) Pull & Start Docker Containers\n'
                                          '2) Stop Containers\n\n\n'
                                          '\033[1;32mYour Selection >>\033[1;m')
                if vuln_net_opts == '1':
                    self.docker_pull_and_run_images('dvwa')
                    self.docker_pull_and_run_images('mimdebian')
                    break
            elif docker_opt == 'back':
                main()

    def auto_install_docker(self):

        sys_commands = ['export DEBIAN_FRONTEND="noninteractive"',
                        'apt-get update',
                        'apt-get purge lxc-docker*',
                        'apt-get purge docker.io*',
                        'apt-get install -y apt-transport-https ca-certificates',
                        'apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 '
                        '--recv-keys 58118E89F3A912897C070ADBF76221572C52609D',
                        """cat > /etc/apt/sources.list.d/docker.list <<'EOF'\
                        deb https://apt.dockerproject.org/repo debian-stretch main
                        EOF""",
                        'apt-get update',
                        'apt-get -y install docker-engine',
                        'service docker start',
                        'docker run hello-world',
                        'groupadd docker',
                        'gpasswd -a ${USER} docker',
                        'service docker restart',
                        'systemctl enable docker'
                        ]
        for cmds in sys_commands:
            os.system(cmds + ';')

    def docker_pull_and_run_images(self, cont_name):
        print 'Pulling docker image..\n\n'
        if cont_name == 'dvwa':
            os.system('sudo docker pull netsecframework/dvwa:vulnstackone')
            print 'Starting container...\n\n'
            os.system('sudo docker run -d -p 80:80 netsecframework/dvwa:vulnstackone')
            print '\033[1;32mNavigate to http://localhost . Click Create/Reset Database.\n' \
                  'Default credentials are admin/password.\033[1;m'
        elif cont_name == 'meta':
            os.system('docker pull netsecframework/metasploitable')
            print 'Starting container...\n\n'
            os.system('docker run -d netsecframework/metasploitable')
        elif cont_name == 'nowasp':
            os.system('sudo docker pull netsecframework/nowasp:latest')
            print 'Starting container...\n\n'
            os.system('sudo docker run -d -p 80:80 netsecframework/nowasp')
            print '\033[1;32mNavigate to http://localhost . Click Create/Reset Database.\n' \
                  'Default credentials are admin/password.\033[1;m'
        elif cont_name == 'mimdebian':
            os.system('sudo docker pull netsecframework/mimdebian:latest')
            print 'Starting container...\n\n'
            os.system('sudo docker run -dit netsecframework/mimdebian')
            os.system('cd lib && sudo docker build -t traffic .')
            os.system('sudo docker run -d traffic')
        elif cont_name == 'kali':
            os.system('sudo docker pull kalilinux/kali-linux-docker')
            print 'Starting container...\n\n'
            os.system('sudo docker run -dit kalilinux/kali-linux-docker')

    def docker_find_container(self, cont_name):
        print '\033[1;32mFinding Docker container...\n\033[1;m'
        if cont_name == 'dvwa':
            proc = subprocess.Popen(["sudo docker ps | grep -i 'netsecframework/dvwa'"], stdout=subprocess.PIPE,
                                    shell=True)
            (out, err) = proc.communicate()
            find_container_id = out.split()
            try:
                return str(find_container_id[0])
            except IndexError:
                print 'No Containers running..'
        elif cont_name == 'nowasp':
            proc = subprocess.Popen(["sudo docker ps | grep -i 'netsecframework/nowasp'"], stdout=subprocess.PIPE,
                                    shell=True)
            (out, err) = proc.communicate()
            find_container_id = out.split()
            try:
                return str(find_container_id[0])
            except IndexError:
                print 'No Containers running..'
        elif cont_name == 'meta':
            proc = subprocess.Popen(["sudo docker ps | grep -i 'netsecframework/metasploitable'"],
                                    stdout=subprocess.PIPE,
                                    shell=True)
            (out, err) = proc.communicate()
            find_container_id = out.split()
            try:
                return str(find_container_id[0])
            except IndexError:
                print 'No Containers running..'
        elif cont_name == 'mimdebian':
            proc = subprocess.Popen(["sudo docker ps | grep -i 'netsecframework/mimdebian'"], stdout=subprocess.PIPE,
                                    shell=True)
            (out, err) = proc.communicate()
            find_container_id = out.split()
            try:
                return str(find_container_id[0])
            except IndexError:
                print 'No Containers running..'
        elif cont_name == 'kali':
            proc = subprocess.Popen(["sudo docker ps | grep -i 'kalilinux/kali-linux-docker'"], stdout=subprocess.PIPE,
                                    shell=True)
            (out, err) = proc.communicate()
            find_container_id = out.split()
            try:
                return str(find_container_id[0])
            except IndexError:
                print 'No Containers running..'

    def docker_shutdown_container(self, cont_name):
        if cont_name == 'dvwa':
            cmd = "sudo docker kill {container}".format(container=self.docker_find_container('dvwa'))
            proc = subprocess.Popen([str(cmd)], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print '\n\033[1;32mContainer off..\033[1;m'
        elif cont_name == 'meta':
            cmd = "sudo docker kill {container}".format(container=self.docker_find_container('meta'))
            proc = subprocess.Popen([str(cmd)], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print '\n\033[1;32mContainer off..\033[1;m'
        elif cont_name == 'nowasp':
            cmd = "sudo docker kill {container}".format(container=self.docker_find_container('nowasp'))
            proc = subprocess.Popen([str(cmd)], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print '\n\033[1;32mContainer off..\033[1;m'
        elif cont_name == 'mimdebian':
            cmd = "sudo docker kill {container}".format(container=self.docker_find_container('mimdebian'))
            proc = subprocess.Popen([str(cmd)], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print '\n\033[1;32mContainer off..\033[1;m'
        elif cont_name == 'kali':
            cmd = "sudo docker kill {container}".format(container=self.docker_find_container('kali'))
            proc = subprocess.Popen([str(cmd)], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print '\n\033[1;32mContainer off..\033[1;m'
