while true; do
    python manage.py runserver

    if [ $? -eq 0 ]; then
        break
    else
        echo "Command failed. Retrying..."
        sleep 0.5
    fi
done
