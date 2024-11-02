---
title: Squid
created: '2024-11-02T06:58:04.328Z'
modified: '2024-11-02T07:01:11.708Z'
---

# Squid

acl --> access control list.

allowing access from local networks:
  acl localnet src 192.168.0.0/16 

acl SSL_ports port 443
acl Safe_ports port 80          # http
acl Safe_ports port 21          # ftp


