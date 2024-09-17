# qbittorrent-telegram-notification-windows
Sends a notification to your Telegram when a download is completed in qbittorrent.

### pre-requisite:

* You will need to install python
* Install requests from cmd
  
  ```pip install requests```

### Instructions:
  
  1. Download notify.py and save it in ur preferred directory
     eg.``` C:\notify.py```
  2. Enter your **bot_token** and **chat_id** on the notify.py.
     - Use BotFather to get your **bot_token** and **chat_id**
  3. Open Qbittorrent and go to Settings>Downloads scroll down and tick **Run on torrrent finished**
  4. Put cmd.exe /C <notify.py location
     eg.` cmd.exe /C C:\notify.py`
  5. Done
