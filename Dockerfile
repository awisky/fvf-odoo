FROM odoo:14

USER root
# Mount Customize /mnt/"addons" folders for users addons
RUN mkdir -p /mnt/odoo

# Update aptitude with new repo
RUN apt-get update \
    && apt-get install -y git

COPY ./config/odoo.conf /etc/odoo/
COPY ./requirements.txt /mnt/odoo/
ADD ./addons /mnt/odoo/addons
ADD ./addons_external /mnt/odoo/addons_external
# Install Chromium
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        python3-dev \
        python3-wheel \
        chromium \
    && pip3 install --upgrade pip \
    && pip3 install -r /mnt/odoo/requirements.txt

RUN chown -R odoo /mnt/*

USER odoo
