sudo apt install nginx

pip3 install gunicorn --break-system-packages

Navegamos hasta la carpeta:
gunicorn --bind 127.0.0.1:8000 app:app

Solución Zakaria:
gunicorn -b 127.0.0.1:8000 app:app 

Ahora creamos un servicio para que gunicorn funcione solo
(sin ejecutarlo manualmente):

sudo nano /etc/systemd/system/miweb.service

Colocamos esto:
---
[Unit]
Description=Gunicorn for miweb
After=network.target

[Service]
User=josevicente
WorkingDirectory=/home/josevicente/Escritorio/miweb
ExecStart=/home/josevicente/.local/bin/gunicorn -b 127.0.0.1:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
---
Control + O / Control + X

Ahora convertimos ese archivo de conf en un servicio
sudo systemctl daemon-reload
sudo systemctl enable miweb
sudo systemctl start miweb
sudo systemctl status miweb


