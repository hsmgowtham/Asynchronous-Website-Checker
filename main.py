import http
import asyncio
import aiohttp
import subprocess
import time


from logger_config import get_logger

# Get logger instance
logger = get_logger(__name__)


async def check_site(session, url):
    try:
        async with session.get(url) as response:
            return url, response.status
    except aiohttp.ClientError as e:
        print(f'Error checking {url}: {e}')
        return url, None


async def main():
    urls = ['https://atlas.my.salesforce-sites.com/SiteLogin?country=India&language=en_US']
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [check_site(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            for url, status in results:
                if status is not None and status==200:
                    logger.info(f'{url} returned status code {status}')
                    subprocess.Popen(['notify-send', 'System Alert', f'The URL is Working Fine!'])
                else:
                    logger.error(f'{url} could not be checked {status}')
                    subprocess.Popen(['notify-send', 'System Alert', f'The URL is Under Maintainance!'])
            time.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())



# define the condition that triggers the notification
threshold = 10

# check the current system load average
load_average = float(subprocess.check_output(["awk '{print $1}' /proc/loadavg"], shell=True))

# send a notification if the condition is met
if load_average > threshold:
    subprocess.Popen(['notify-send', 'System Alert', f'System load average is {load_average:.2f}!'])



