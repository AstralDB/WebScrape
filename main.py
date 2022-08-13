import requests
import re
import textwrap
import github
from github import Github

client, results, pattern = Github('YOUR API KEY'), [], re.compile(r'https://discord.com/api/webhooks/\d{18}/[^\n]*')
search = client.search_code('in:file discord.com/api/webhooks/', sort='indexed', order='desc', highlight=True)

try:
    for file in search:
        get = requests.get(file.download_url).text
        data = re.findall(pattern, get)
        results.extend(data)
except github.RateLimitExceededException: raise('Rate limited')

for item in results:
    webhook = textwrap.shorten(item, width=120, fix_sentence_endings=True, break_long_words=True, break_on_hyphens=False, placeholder='')

    try: requests.get(webhook).json()['id']
    except: continue
     
    finally:
        response = requests.get(webhook).json()
        print('Webhook_URL: %s' % webhook)
        print('Token: %s' % response['token'])
        print('Name: %s' % response['name'])
