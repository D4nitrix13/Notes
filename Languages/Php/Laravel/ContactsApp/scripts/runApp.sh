#!/bin/sh

# export HOST=0.0.0.0
# export PORT=3000

npm run watch &>/dev/null &
php artisan key:generate
sleep 3; php artisan migrate
php artisan serve --host=0.0.0.0 --ansi -vvv --tries 10