#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app

# apache
sys.path.insert(0, abspath(dirname(__file__)))
# what is application
application = app.app

"""
建立一个软连接
ln -s /root/web13/todo.conf /etc/supervisor/conf.d/todo.conf


[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
autorestart=true
"""
