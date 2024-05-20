FROM hub.test.ru:5000/tess_example

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 14219A96E15E78F4 \
    && curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash \
    && apt-get install -y gitlab-runner \
    && sed -i -e 's/mesg n .*true/tty -s \&\& mesg n/g' /root/.profile

RUN apt-get update -qq \
    && apt-get -y install openssh-client openssh-server \
    && echo "PasswordAuthentication no" >> /etc/ssh/sshd_config \
    && mkdir ~/.ssh; chmod u=rwx,go= ~/.ssh \
    && true > ~/.ssh/authorized_keys; chmod u=rw,go=r ~/.ssh/authorized_keys \
    && echo 'ssh-rsa AAAAexample' >> ~/.ssh/authorized_keys \
    && true

RUN apt-get -y install python3.8 && apt-get -y install python3-pip && pip3 install pipenv

ENV LANG C.UTF-8

ADD entrypoint.sh /usr/local/bin/
CMD ["entrypoint.sh"]