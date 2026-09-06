bind = "127.0.0.1:8000"

workers = 3
timeout = 30
graceful_timeout = 30
keepalive = 5

accesslog = "-"
errorlog = "-"
capture_output = True
loglevel = "info"

preload_app = True
