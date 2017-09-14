#!/usr/bin/env python
import os
import socket
import sys

if __name__ == "__main__":
    if socket.gethostname() == 'ubuntu-512mb-sgp1-01':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petManagement.production_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petManagement.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
