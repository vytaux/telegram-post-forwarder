# Telegram Post Forwarder

This script forwards a channel message containing a specific text to a user-specified group.

## Configuration Setup

Before running the script, make sure to set up your configuration file. The script uses a `config.ini` file to store sensitive information like API credentials and group IDs. You can use the provided `config.ini.sample` as a template:

1. **Create a Configuration File**:
  - Copy the sample config to a new file:
    ```bash
    cp config.ini.sample config.ini
    ```
  - Open `config.ini` and fill in the required values.
    Go to https://my.telegram.org and log in with your phone number to obtain your API ID and API HASH. These are required to connect to Telegram's API.

    ```
    [TELEGRAM]
    API_ID = YOUR_API_ID_HERE
    API_HASH = YOUR_API_HASH_HERE
    PHONE_NUMBER = YOUR_PHONE_NUMBER_HERE

    [GROUPS]
    USER_ID_TO_FORWARD = USER_ID_TO_FORWARD_HERE
    TARGET_GROUP_ID = TARGET_GROUP_ID_HERE
    ORIGINAL_GROUP_ID = ORIGINAL_GROUP_ID_HERE
    ```

## 1. **Run the Script**

Once the `config.ini` file is filled with your credentials, you can run the script.

Start by installing the dependencies with:
```bash
pip install -r requirements.txt
```
Then run the script with:
```bash
python main.py
```

## 2. **Optional: Install the Systemd Startup Script**

If you want to run the script as a service that starts automatically, you can install and enable the `systemd` service for the Telegram Post Forwarder:

Run the following commands:

```bash
sudo cp ./systemd/telegram_post_forwarder.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable telegram_post_forwarder.service
sudo systemctl start telegram_post_forwarder.service
```

---

## 3. **Check the Service Status**

To verify that the service is running properly, check its status with:

```bash
sudo systemctl status telegram_post_forwarder.service
```

You should see output indicating that the service is **active (running)**.

---

## Notes

- Ensure that the `WorkingDirectory` specified in the `telegram_post_forwarder.service` file matches the directory where your script is located.
- If you encounter any issues, check the service logs with:
  ```bash
  sudo journalctl -u telegram_post_forwarder.service
  ```