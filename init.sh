#!/bin/sh
set -e
docker-compose up -d
echo 'Sleeping 10s - don`t forget KISS principle'
sleep 10
docker-compose exec tile /usr/local/sbin/run initdb startdb createuser createdb
docker-compose exec tile sh -c 'sudo -upostgres psql -d gis -c "TRUNCATE spatial_ref_sys"'
docker-compose exec tile sh -c 'sudo -upostgres psql -d gis -f /usr/share/postgresql/9.3/contrib/postgis-2.1/spatial_ref_sys.sql'
# import file naming MUST be import.osm
docker-compose exec tile /usr/local/sbin/run import
docker-compose restart
echo 'Wait a bit & check tiles' 
