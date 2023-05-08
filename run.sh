docker run \
    --name madi_test_filebrowser \
    -d \
    --rm \
    -v /home/madi/Desktop/projects/filebrowser_test/data:/srv \
    -v /home/madi/Desktop/projects/filebrowser_test/madi.db:/database/filebrowser.db \
    -v /home/madi/Desktop/projects/filebrowser_test/settings.json:/config/settings.json \
    -e PUID=$(id -u) \
    -e PGID=$(id -g) \
    -p 8080:80 \
    filebrowser/filebrowser:v2.23.0