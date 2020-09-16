#!/usr/local/bin/bash
# This file contains the install script for sabnzbd

# Check if dataset Downloads dataset exist, create if they do not.
# shellcheck disable=SC2154
createmount "$1" "${global_dataset_downloads}" /mnt/Downloads

# Check if dataset Complete Downloads dataset exist, create if they do not.
createmount "$1" "${global_dataset_downloads}"/Complete /mnt/Downloads/Complete

# Check if dataset InComplete Downloads dataset exist, create if they do not.
createmount "$1" "${global_dataset_downloads}"/Incomplete /mnt/Downloads/Incomplete

# Force update pkg to get latest sabnzbd version
iocage exec "$1" pkg update
iocage exec "$1" pkg install sabnzbdplus
iocage exec "$1" service sabnzbd start
iocage exec "$1" sysrc "sabnzbd_enable=YES"
iocage exec "$1" sysrc "sabnzbd_conf_dir=/config"
iocage exec "$1" chown -R sabnzbd:sabnzbd /config
iocage exec "$1" service sabnzbd restart

echo "Finished installing sabnzbd"
