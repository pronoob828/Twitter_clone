echo "Build Start"
sqlite3
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "Build End"