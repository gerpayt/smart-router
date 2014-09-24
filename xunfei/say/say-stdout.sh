#/bin/sh
./say-stdout $1 | mplayer -cache 256 - > /dev/null 2>&1
