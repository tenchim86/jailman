#!/usr/local/bin/bash
# This file contains the install script for sabnzbd

# Check if dataset Downloads dataset exist, create if they do not.
# shellcheck disable=SC2154
createmount "$1" "${global_dataset_downloads}" /mnt/Downloads

# Check if dataset Complete Downloads dataset exist, create if they do not.
createmount "$1" "${global_dataset_downloads}"/Complete /mnt/Downloads/Complete

# Check if dataset InComplete Downloads dataset exist, create if they do not.
createmount "$1" "${global_dataset_downloads}"/Incomplete /mnt/Downloads/Incomplete


iocage exec "$1" chown -R sabnzbd:sabnzbd /config
iocage exec "$1" sysrc "sabnzbdn_enable=YES"
iocage exec "$1" sysrc "sabnzbd_conf_dir=/config"
iocage exec "$1" sysrc "sabnzbd_download_dir=/mnt/Downloads/Complete"
iocage exec "$1" service sabnzbd restart
