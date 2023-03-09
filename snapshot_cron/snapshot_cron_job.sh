#!/usr/bin/bash
snapshot_dir=/home/inery-node/inery.setup/master.node/blockchain/data/snapshots
www_dir=/home/snapshot_cron/www
snaps_dir=$www_dir/snaps
js_dir=$www_dir/js
rm -rf $snapshot_dir/*
curl -X POST http://127.0.0.1:8888/v1/producer/create_snapshot
files=($snapshot_dir/*)
filename=$(basename ${files[0]})
rm -rf $snaps_dir/*
cp -r $snapshot_dir/$filename $www_dir/snaps
replace_text="var snapshot_filename = '$filename';"
sed -i "1s/.*/$replace_text/" $js_dir/functions.js
