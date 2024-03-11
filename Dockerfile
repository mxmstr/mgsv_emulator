FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND noninteractive

# Install all required packages in one step
RUN apt-get update && apt-get install -y --allow-downgrades --no-install-recommends \
    wget \
    build-essential \
    zlib1g \
    zlib1g-dev \
    libssl-dev \
    libffi-dev \
    iproute2 \
    net-tools \
    nano \
    curl \
    lsb-release \
    apache2 \
    libapache2-mod-wsgi-py3 \
    gnupg2 \
    python3.11 \
    python3-pip \
    python3.11-dev \
    gcc \
    vim \
    pkg-config \
    protobuf-compiler \
    python3.11-venv && \
    rm -rf /var/lib/apt/lists/*

# Additional setup for Percona
RUN curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb && \
    apt install -y ./percona-release_latest.generic_all.deb && \
    percona-release setup ps80 && \
    apt-get install -y --allow-downgrades --no-install-recommends percona-server-test && \
    apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Python package installations in a virtual environment
RUN apt-get update && apt-get install -y python3.11-venv && \
    python3.11 -m venv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install pymysql requests setuptools wheel protobuf

# Copying files and setting permissions
COPY [ "src/mgsv_emulator", "/var/www/mgsv_server/wsgi-scripts/mgsv_emulator" ]
COPY files/SteamAppTicket_pb.proto /var/www/mgsv_server/wsgi-scripts/mgsv_emulator/
COPY files/myapp.wsgi /var/www/mgsv_server/wsgi-scripts
COPY files/mgs_server.conf /etc/apache2/sites-available/
COPY files/static_key.bin /var/www/mgsv_server/
COPY files/eula.var /var/www/mgsv_server/www/tppstmweb/eula
COPY files/coin.var /var/www/mgsv_server/www/tppstmweb/coin
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/gdpr
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/privacy_jp
COPY files/privacy.var /var/www/mgsv_server/www/tppstmweb/privacy
COPY files/dbBase.sql /dbBase.sql
COPY files/dbMGO3.sql /dbMGO3.sql
COPY files/entrypoint.sh /entrypoint.sh

# Apache and protobuf setup
RUN a2ensite mgs_server && \
    a2dissite 000-default && \
    chmod +x /entrypoint.sh && \
    chown -R www-data:www-data /var/www/mgsv_server && \
    protoc -I=/var/www/mgsv_server/wsgi-scripts/mgsv_emulator \
        --python_out=/var/www/mgsv_server/wsgi-scripts/mgsv_emulator \
        /var/www/mgsv_server/wsgi-scripts/mgsv_emulator/SteamAppTicket_pb.proto

EXPOSE 80
CMD ["/entrypoint.sh"]
