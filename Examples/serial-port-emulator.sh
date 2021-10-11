nohup socat -d -d pty,link=./virtual-tty-recv,raw,echo=0 pty,link=./virtual-tty-send,raw,echo=0 &
echo "Emulating serial port ./virtual-tty-recv..."
python sender.py