FROM centos
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN yum -y install centos-release-scl && yum -y install rh-python35 && LD_LIBRARY_PATH=/opt/rh/rh-python35/root/usr/lib64 /opt/rh/rh-python35/root/usr/bin/pip install mattermostdriver google-api-python-client kubernetes && rm -rf /var/cache/yum

ADD googlecalendar.py /usr/bin
ADD cal2mat.py /usr/bin
ADD crontemplate.yml /usr/bin

RUN chmod o+x /usr/bin/cal2mat.py
ENV LD_LIBRARY_PATH /opt/rh/rh-python35/root/usr/lib64

ENTRYPOINT ["/usr/bin/cal2mat.py"]
