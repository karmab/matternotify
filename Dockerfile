FROM centos
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN yum -y install centos-release-scl cronie sudo && yum -y install rh-python35 && LD_LIBRARY_PATH=/opt/rh/rh-python35/root/usr/lib64 /opt/rh/rh-python35/root/usr/bin/pip install mattermostdriver && rm -rf /var/cache/yum

RUN useradd -u 10001 -m -d /home/matter matter
ADD notify.py /usr/bin
ADD start.sh /usr/bin
ADD sudo_matter /etc/sudoers.d
RUN export TZ=Europe/Madrid && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN chmod u+x /usr/bin/start.sh && chmod o+x /usr/bin/notify.py && sed -i '/session required pam_loginuid.so/d' /etc/pam.d/crond

USER 10001
ENTRYPOINT  ["/usr/bin/start.sh"]
