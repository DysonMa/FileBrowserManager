docker run \
    --name test_filebrowser \
    -d \
    --rm \
    -v ./data:/srv \
    -v ./filebrowser.db:/database/filebrowser.db \
    -v ./settings.json:/config/settings.json \
    -e PUID=$(id -u) \
    -e PGID=$(id -g) \
    -p 8080:80 \
    filebrowser/filebrowser:v2.23.0