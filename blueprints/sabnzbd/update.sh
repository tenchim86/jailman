#!/usr/local/bin/bash
# This file contains the update script for sonarr

iocage exec "$1" service sabnzbd stop
#TODO insert code to update sabnzbd itself here
iocage exec "$1" chown -R sabnzbd:sabnzbd /usr/local/share/NzbDrone /config
# shellcheck disable=SC2154
cp "${SCRIPT_DIR}"/blueprints/sabnzbd/includes/sabnzbd.rc /mnt/"${global_dataset_iocage}"/jails/"$1"/root/usr/local/etc/rc.d/sabnzbd
iocage exec "$1" chmod u+x /usr/local/etc/rc.d/sabnzbd
iocage exec "$1" service sabnzbd restart
