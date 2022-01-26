FROM odoo:13

USER root
# Mount Customize /mnt/"addons" folders for users addons
RUN mkdir -p /mnt/odoo

RUN mkdir -p /mnt/odoo \
    && mkdir -p /mnt/odoo/addons_oca \
    && mkdir -p /mnt/odoo/addons_local \
    && mkdir -p /mnt/odoo/addons_external

# Install Chromium
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        python3-dev \
        python3-wheel \
        chromium \
    && pip3 install --upgrade pip

# Update aptitude with new repo
RUN apt-get update \
    && apt-get install -y git \
    build-essential autoconf libtool swig

WORKDIR /mnt/odoo/addons_local
# Calyx addons
RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/FedericoGregori/account_debt_management.git
# ADHOC modules
RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/account-financial-tools.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/account-invoicing.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/account-payment.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/aeroo_reports.git

RUN pip3 install -r aeroo_reports/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/argentina-sale.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/miscellaneous.git

RUN pip3 install -r miscellaneous/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/odoo-argentina.git

RUN pip3 install -r odoo-argentina/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/odoo-argentina-ce.git

RUN pip3 install -r odoo-argentina-ce/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/product.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/sale.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/stock.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/ingadhoc/website.git

RUN pip3 install -r website/requirements.txt

WORKDIR /mnt/odoo/addons_oca
# OCA modules
RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/account-analytic.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/account-financial-reporting.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/account-financial-tools.git

RUN pip3 install -r account-financial-tools/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/contract.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/hr-expense.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/mis-builder.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/partner-contact.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/queue.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/reporting-engine.git

RUN pip3 install -r reporting-engine/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/sale-workflow.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/server-brand.git

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/server-ux.git

RUN pip3 install -r server-ux/requirements.txt

RUN git clone --progress --verbose -b 13.0 --single-branch --depth 1 \
    https://github.com/OCA/web.git

RUN pip3 install -r web/requirements.txt

WORKDIR /
COPY ./config/odoo.conf /etc/odoo/
COPY ./requirements.txt /mnt/odoo/
ADD ./addons /mnt/odoo/addons
ADD ./addons_external /mnt/odoo/addons_external
# Install Chromium
RUN pip3 install -r /mnt/odoo/requirements.txt

RUN chown -R odoo /mnt/*
RUN chown -R odoo /var/lib/odoo
#USER odoo
