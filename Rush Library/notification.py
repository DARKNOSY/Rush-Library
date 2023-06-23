# by me

from plyer import notification

async def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
    print("Desktop notification sent.")

asyncio.run(send_notification("Notification Title", "Notification Message"))
