#!/bin/bash

echo "Start deploy"
ssh -tq root@213.239.193.208 '/bin/bash -l -c "source ~/.nvm/nvm.sh; cd /var/www/ergodocs/tools; git pull; rm -rf /site;  mkdocs build;"'
echo "Deployed Successfully!"

exit 0
