josevicente@josevicenteportatil:~$ sudo service mongod status
● mongod.service - MongoDB Database Server
     Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled; preset: e>
     Active: active (running) since Wed 2026-01-28 08:08:30 CET; 58min ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 5185 (mongod)
     Memory: 301.6M (peak: 365.5M)
        CPU: 14.943s
     CGroup: /system.slice/mongod.service
             └─5185 /usr/bin/mongod --config /etc/mongod.conf

ene 28 08:08:30 josevicenteportatil systemd[1]: Started mongod.service - MongoD>
ene 28 08:08:30 josevicenteportatil mongod[5185]: {"t":{"$date":"2026-01-28T07:>
lines 1-12/12 (END)
