#!/bin/sh
# gunicorn 启动 superset (后期使用 superversior 控制)

SERVER_NAME="superset app"
SERVER_APP_NAME="superset.app:create_app()"

check_server_pid()
{
    echo ` ps -efww | grep -v 'grep' | grep "${SERVER_APP_NAME}" | awk '{print $2}' `
}

start_server()
{
    #gunicorn --workers 5 --timeout 120 --bind 0.0.0.0:8088 "${SERVER_APP_NAME}" --daemon
    gunicorn --workers 5 --timeout 120 --worker-connections=1000 --bind 0.0.0.0:8088 "${SERVER_APP_NAME}"
}

start()
{
    pid=$(check_server_pid)
    if [ -n "$pid" ]; then
        echo "Warning: $SERVER_NAME already started! (pid: $pid)"
    else
        echo -n "Starting $SERVER_NAME ..."
        start_server
        sleep 1
        pid=$(check_server_pid)
        if [ -n "$pid" ]; then
            echo "(pid: $pid) [OK]"
        else
            echo "[Failed]"
        fi
    fi
}

stop()
{
    pid=$(check_server_pid)
    if [ -n "$pid" ]; then
        echo -n "Stopping $SERVER_NAME ...(pid: $pid)"
        kill $pid &>/dev/null
        sleep 1
        pid=$(check_server_pid)
        if [ -z "$pid" ]; then
            echo "[OK]"
        else
            echo "[Failed]"
        fi
    else
        echo "Warning: $SERVER_NAME is not running"
        fi
}

case "$1" in
    'start')
        start
        ;;
    'stop')
        stop
        ;;
    'restart')
        stop
        start
    ;;
    *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
esac
