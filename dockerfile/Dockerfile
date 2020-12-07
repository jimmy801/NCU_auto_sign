ARG ubuntu=16.04
FROM ubuntu:$ubuntu
ARG PYTHON_VERSION=3

WORKDIR home

# install packages
RUN apt-get update && \
    apt-get install -y \
        cmake \
        wget \
        curl \
        git \
        vim \
        software-properties-common \
        zip \
        gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# download chrome & chrome driver
RUN deb=google-chrome-stable_current_amd64.deb && \
	wget https://dl.google.com/linux/direct/$deb && \
	dpkg -i $deb && rm $deb && \
	driver_version=$(google-chrome --version) && \
	driver_version=${driver_version##*Google Chrome} && \
	# remove leading whitespace characters
	driver_version="${driver_version#"${driver_version%%[![:space:]]*}"}" && \
	# remove trailing whitespace characters
	driver_version="${driver_version%"${driver_version##*[![:space:]]}"}" && \
	wget https://chromedriver.storage.googleapis.com/$driver_version/chromedriver_linux64.zip && \
	unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip && \
	mv chromedriver /usr/bin

# register python dependency(ppa)
# NOTE: Register ppa may take more time
# More info: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
# Note: Python2.7 (all), 
#       Python 3.5 (16.04, xenial), Python 3.6 (18.04, bionic), Python 3.8 (20.04, focal) 
#       are not provided by deadsnakes as upstream ubuntu provides those packages
#       (it means they don't need to register ppa)
RUN ubuntu=$(lsb_release -a | grep "Release:") && ubuntu=${ubuntu##*:} && \
    if [ "$PYTHON_VERSION" != "2.7" ] && [ "$PYTHON_VERSION" != "3" ] && \
       [ \( ${ubuntu} = "16.04" -a "$PYTHON_VERSION" != "3.5" \) -o \
       \( ${ubuntu} = "18.04" -a "$PYTHON_VERSION" != "3.6" \) -o \
       \( ${ubuntu} = "20.04" -a "$PYTHON_VERSION" != "3.8" \) ]; then \
           add-apt-repository ppa:deadsnakes/ppa && \
           apt-get update; \
    fi

# install specific python version
RUN apt-get install -y \
        python$PYTHON_VERSION \
        python$PYTHON_VERSION-dev && \
    # set default `python` to `python$PYTHON_VERSION`
    ln -sf /usr/bin/python$PYTHON_VERSION /usr/bin/python

# install pip
RUN if [ $PYTHON_VERSION \> 3 ]; then \
        apt-get install -y python3-distutils-extra && \
        ln -sf /usr/bin/python$PYTHON_VERSION /usr/bin/python3; \
    fi && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# set ~/.bashrc
RUN sed -i '53,/PS1/c \
    '"\    PS1=\'\$\{debian_chroot:\+\(\$debian_chroot\)\}\\\[\\\033\[01;32m\\\]\\\u\\\[\\\033\[00;37m\\\]@\\\[\\\033\[01;35m\\\]\\\h\\\[\\\033\[00m\\\]:\\\[\\\033\[01;34m\\\]\\\w\\\[\\\033\[00m\\\]# \'"\\nelse\\n"    PS1=\'\$\{debian_chroot:\+\(\$debian_chroot\)\}\\\u@\\\h:\\\w# \'"'\
' ~/.bashrc && \
    sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' ~/.bashrc
    # above enable color prompt of docker in terminal