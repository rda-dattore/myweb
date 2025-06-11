# syntax=docker/dockerfile:1

FROM dattore/gdex-web-portal:python

# create and activate virtual environment
RUN python3.11 -m venv /usr/local/gdexweb
ENV PATH=/usr/local/gdexweb/bin:$PATH

# install and set up wagtail
RUN pip install wagtail==7.0 Django==5.2 wagtailmenus==3.1.9
RUN wagtail start gdexwebserver /usr/local/gdexweb
RUN pip install -r /usr/local/gdexweb/requirements.txt
RUN python /usr/local/gdexweb/manage.py makemigrations
RUN python /usr/local/gdexweb/manage.py migrate
RUN python /usr/local/gdexweb/manage.py collectstatic --noinput

# install database tools
RUN apt-get install -y libpq-dev postgresql
RUN pip install psycopg2

# install the web tools
RUN apt-get install -y apache2 apache2-dev
RUN apt-get install -y php php-cli php-pgsql
RUN pip install mod_wsgi
RUN ln -s /usr/local/gdexweb/lib/python3.11/site-packages/mod_wsgi/server/mod_wsgi-py311.cpython-311-x86_64-linux-gnu.so /usr/lib/apache2/modules/mod_wsgi_python3.11.so

# create the apache configuration
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist
RUN <<EOF
cat <<EOFCAT> /etc/apache2/apache2.conf
ServerRoot "/etc/apache2"
ServerName gdexweb.ucar.edu
Listen 0.0.0.0:8080

DefaultRuntimeDir \${APACHE_RUN_DIR}

PidFile \${APACHE_PID_FILE}

Timeout 300

KeepAlive On

MaxKeepAliveRequests 100

KeepAliveTimeout 5

User \${APACHE_RUN_USER}
Group \${APACHE_RUN_GROUP}

HostnameLookups Off

ErrorLog \${APACHE_LOG_DIR}/error.log
LogLevel warn
LogFormat "%v:%p %h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined
LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
LogFormat "%h %l %u %t \"%r\" %>s %O" common
LogFormat "%{Referer}i -> %U" referer
LogFormat "%{User-agent}i" agent

IncludeOptional mods-enabled/*.load
IncludeOptional mods-enabled/*.conf

Include ports.conf

<Directory />
        Options FollowSymLinks
        AllowOverride None
        Require all denied
</Directory>
<Directory /usr/share>
        AllowOverride None
        Require all granted
</Directory>

<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>

AccessFileName .htaccess
<FilesMatch "^\.ht">
        Require all denied
</FilesMatch>

IncludeOptional conf-enabled/*.conf

IncludeOptional sites-enabled/*.conf

EOFCAT
EOF

RUN <<EOF
cat <<EOFCAT> /etc/apache2/mods-enabled/wsgi.load
LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi_python3.11.so
EOFCAT
EOF

RUN mv /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf.dist
RUN <<EOF
cat <<EOFCAT> /etc/apache2/sites-enabled/000-default.conf
<VirtualHost *:8080>
        ServerAdmin rdahelp@ucar.edu
        DocumentRoot /usr/local/gdexweb

        <Directory /usr/local/gdexweb>
            Require all granted
        </Directory>

        IncludeOptional conf-enabled/aliases.conf

        WSGIDaemonProcess gdexweb python-path=/usr/local/gdexweb:/usr/local/gdexweb/lib/python3.11/site-packages request-timeout=180
        WSGIScriptAlias / /usr/local/gdexweb/gdexwebserver/wsgi.py
        WSGIProcessGroup gdexweb
        WSGIApplicationGroup %{GLOBAL}

        ErrorLog \${APACHE_LOG_DIR}/error.log
        CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

EOFCAT
EOF

RUN mkdir /data
RUN chown www-data:www-data /data
# set permissions
RUN chown -R www-data:www-data /usr/local/gdexweb
RUN touch /var/log/django.log
RUN chown www-data:www-data /var/log/django.log

RUN pip install gunicorn
ENV PYTHONPATH=/usr/local/gdexweb
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--capture-output", "--log-file", "/var/log/gunicorn.log", "gdexwebserver.wsgi"]

# start the apache web server
#CMD ["apache2ctl", "-D", "FOREGROUND"]
