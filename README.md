## RUN Odoo Using Docker
```
cd odoo
docker compose up -d
```

## Login Information
```
Database: database_odoo
Master Password: odoo
Password: odoo
```

## Run Unit Testing

```
docker exec -it codingtest-odoo-1 /bin/bash
cd /usr/bin
odoo -i material_system --test-enable -p 7777
odoo --test-file=mnt/addons/material_system/tests/test_material.py -p 7788
```

## Addons of Odoo Directory
```
/usr/lib/python3/dist-packages/odoo/addons
```
