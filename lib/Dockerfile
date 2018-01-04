FROM netsecframework/mimdebian:latest
ENTRYPOINT ["/bin/bash", "-c", "service cron start"]
ENTRYPOINT ["/bin/bash", "-c","service rsyslog start"]
ENTRYPOINT ["/bin/bash", "-c","python /root/py_request.py"]
