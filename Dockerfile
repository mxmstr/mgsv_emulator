FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --allow-downgrades --no-install-recommends \
                    net-tools \
                    nano \
                    curl \
                    lsb-release \
                    zlib1g=1:1.2.8.dfsg-5 \
                    zlib1g-dev \
                    libmariadbclient-dev \
                    libmariadbclient-dev-compat \
                    default-libmysqlclient-dev \
    				apache2 \
                    python3 \
                    libapache2-mod-wsgi-py3 \
                    wget \
                    gnupg2 \
                    python3-pip \
                    gcc \
                    python3-dev \
                    libssl-dev \
                    vim \
    && wget https://repo.percona.com/apt/percona-release_latest.stretch_all.deb \
    && dpkg -i percona-release_latest.stretch_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends percona-server-server-5.7 libperconaserverclient20 \
    && mkdir -p /var/www/mgsv_server/wsgi-scripts/mgsv_emulator \
    && mkdir -p /var/www/mgsv_server/logs \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/eula \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/coin \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/gdpr \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/privacy_jp \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/privacy \
    && touch /var/log/app.log /var/www/mgsv_server/logs/access.log /var/log/error.log \
    && pip3 install requests setuptools wheel \
    && pip3 install mysqlclient \
    && chown www-data:www-data /var/log/app.log /var/log/error.log
COPY [ "src/mgsv_emulator", "/var/www/mgsv_server/wsgi-scripts/mgsv_emulator" ]
COPY files/myapp.wsgi /var/www/mgsv_server/wsgi-scripts
COPY files/mgs_server.conf /etc/apache2/sites-available/
COPY files/static_key.bin /var/www/mgsv_server/
COPY files/eula.var /var/www/mgsv_server/www/tppstmweb/eula
COPY files/coin.var /var/www/mgsv_server/www/tppstmweb/coin
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/gdpr
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/privacy_jp
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/privacy
COPY files/database.sql /database.sql
COPY files/entrypoint.sh /entrypoint.sh
RUN a2ensite mgs_server \
	&& a2dissite 000-default \
	&& chmod +x /entrypoint.sh \
	&& rm /percona-release_latest.stretch_all.deb \
	&& chown -R www-data:www-data /var/www/mgsv_server
EXPOSE 80
CMD ["/entrypoint.sh"]