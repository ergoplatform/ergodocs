#!/bin/bash

echo "Start deploy"
ssh -tq root@88.198.50.217 '/bin/bash -l -c "source ~/.nvm/nvm.sh; cd /var/www/html/ergodocs; git pull; rm -rf /site;  mkdocs build"'
echo "Deployed Successfully!"

exit 0
