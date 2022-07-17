FROM jboss/keycloak

USER root

RUN mkdir -p /etc/x509/https && \
    chrgp 1000 /etc/x509/https && \
    chown 1000 /etc/x509/https &&

COPY entrypoint.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/loca/bin/entrypoint.sh"]

USER 1000

ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]