FROM postgres:9.6-bullseye
ENV DEBIAN_FRONTEND=noninteractive
RUN /bin/sh -c "apt-get update -y && apt-get install locales-all -y && apt-get clean -y && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*"
ENV LC_ALL="pt_BR.UTF-8"
ENV LANG="pt_BR.UTF-8"
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/9.6/bin
EXPOSE 5432
USER postgres
CMD ["postgres"]
