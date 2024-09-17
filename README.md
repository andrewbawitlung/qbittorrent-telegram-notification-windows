# qbittorrent Telegram Notification Windows
Sends a notification to your Telegram when a download is completed in qbittorrent.

### pre-requisite:

* Create a bot using BotFather in telegram

  ``https://t.me/BotFather``
* You will need to install python
* Install requests from cmd
  
  ```pip install requests```

### Instructions:
  
  1. Download notify.py and save it in ur preferred directory

     eg.``` C:\notify.py```
  3. Enter your **bot_token** and **chat_id** on the notify.py.
     - Use BotFather to get your `bot_token` and `chat_id`
  4. Open Qbittorrent and go to Settings>Downloads scroll down and tick **Run on torrrent finished**
  5. Enter cmd.exe /C <notify.py location>

     eg.` cmd.exe /C C:\notify.py`
  7. Done
