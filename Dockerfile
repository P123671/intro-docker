FROM busybox
HEALTHCHECK --interval=5s CMD ping -c 172.17.0.3