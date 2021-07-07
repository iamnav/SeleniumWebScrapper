import constants
from selenium_driver import driver
from notification_client import client
import time


def main():
    driver.get(constants.PRODUCT_URL)

    while True:
        check_website()
        waited_count = 0

        for i in range(5):
            time.sleep(constants.SLEEP_SECS)
            waited_count += 1
            print(f'waited for: {waited_count} minute')


def get_available_text():
    div_name = constants.TARGET_DIV_NAME
    e = driver.find_element_by_css_selector(div_name)
    return e.text


def check_website():
    print('Refreshing the website...')
    driver.refresh()

    try:
        availableText = get_available_text()
        if availableText == constants.SOLD_OUT:
            text_to_send = availableText
        else:
            text_to_send = availableText + ' ' + constants.SLACK_ID
    except Exception as e:
        text_to_send = str(e)

    # client.chat_postMessage(channel='#bottest', text=text_to_send)
    print('Sent a message: ' + text_to_send)
