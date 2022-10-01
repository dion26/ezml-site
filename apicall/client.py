from urllib import response
import requests
from enum import Enum
import asyncio
import aiohttp

endpoint = "http://localhost:8000/api/"

class Base_Url(Enum):
    PLAYER = 'players/'
    TEAM = 'teams/'
    SOCIAL = 'players/social/'
    MEMBERSHIP = 'teams/membership/'

class Client():
    def __init__(self):
        pass

    def create(self, data, base_url):
        url = endpoint+ base_url.value +'create/'
        get_response = requests.post(url, json=data)
        print(get_response.text)
        return get_response.json()
    
    def update(self, data, pid, base_url, slug=''):
        if slug !='':
            url = endpoint+ base_url.value + str(pid) + '/' + slug + '/' + 'update/'
        else:
            url = endpoint+ base_url.value + str(pid) + '/' +'update/'
        get_response = requests.put(url, json=data)
        print(get_response.text)
        return get_response.json()

    async def _send(self, session, url, object, semaphore):
        async with semaphore:
            await session.put(url, json=object)

    def _get_tasks(self, session, objects, base_url, semaphore):
        tasks = []
        for object in objects:
            try:
                slug = object['slug']
            except:
                slug = ''
            pid = object['public_id']
            if slug !='':
                url = endpoint+ base_url.value + str(pid) + '/' + slug + '/' + 'update/'
            else:
                url = endpoint+ base_url.value + str(pid) + '/' +'update/'
            tasks.append(self._send(session, url, object, semaphore))
        return tasks

    async def bulk_update(self, objects, base_url):
        async with aiohttp.ClientSession() as session:
            s = asyncio.Semaphore(value=10)
            tasks = self._get_tasks(session, objects, base_url, s)
            
            response = await asyncio.gather(*tasks)

    def retrive(self, base_url, pid, slug=''):
        if slug !='':
            url = endpoint+ base_url.value + str(pid) + '/' + slug + '/'
        else:
            url = endpoint+ base_url.value + str(pid) + '/'
        get_response = requests.get(url)
        return get_response

    # check if object exists
    async def sort_objects(self, objects, base_url):
        new_object = []
        existing_object = []

        async with aiohttp.ClientSession() as session:
            for object in objects:
                try:
                    slug = object['slug']
                except:
                    slug = ''
                pid = object['public_id']

                if slug !='':
                    url = endpoint+ base_url.value + str(pid) + '/' + slug + '/'
                else:
                    url = endpoint+ base_url.value + str(pid) + '/'
                
                get_response = await session.get(url, ssl=False)
                if get_response.status == 200:
                    existing_object.append(object)
                else:
                    new_object.append(object)

        return (new_object, existing_object)
    
    def list_objects(self, base_url):
        url = endpoint+ base_url.value
        get_response = requests.get(url)
        return get_response.json()