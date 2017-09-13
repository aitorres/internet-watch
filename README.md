# Internet Watch
Welcome to Internet Watch! This is a tiny Python script that watches over your internet connection to detect and register changes in its status on a local, Markdown-ready file.

## Usage
You should run Internet Watch often, either manually or using cron jobs or any other task scheduler. It compares your internet status with the prior status, and if it finds a change, it registers the change on this file.

You can tweak the amount of tries, which is 10 by default.