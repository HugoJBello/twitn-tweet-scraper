pm2 stop twitter
pm2 delete twitter
pm2 start "pipenv run python3 main.py" --name "twitter"
