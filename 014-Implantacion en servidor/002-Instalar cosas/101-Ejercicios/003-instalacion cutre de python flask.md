En el servidor ya tenemos python3
Pero no tenemos pip

sudo apt install python3-pip
pip3 install flask --break-system-packages

cd /home/jocarsa

mkdir proyectoflask1

cd proyectoflask1

Parar apache:
sudo service apache2 stop

sudo shutdown