pkill tmux
tmux new-session -d -s server 'git fetch && git reset origin/main --hard && python -m venv python3-virtualenv && source python3-virtualenv/bin/activate && pip install -r requirements.txt && flask run --host=0.0.0.0 --port=80'
