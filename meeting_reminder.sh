#!/usr/bin/env bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    2>/dev/null)

echo $meeting_info

if [[ -n "$meeting_info" ]]; then
    python3 send_reminder.py "$meeting_info"
fi
