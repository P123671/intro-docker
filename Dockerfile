FROM rockylinux:9

# Update and install without forcing specific packages
RUN dnf update -y && \
    dnf install -y \
    sudo \
    wget \
    vim-enhanced \
    git \
    epel-release \
    && dnf clean all

WORKDIR /app

CMD ["/bin/bash"]