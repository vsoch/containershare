#!/usr/bin/env python

import requests
import hashlib
import os
import sys

endpoint = os.environ.get('ENDPOINT')
containershare = os.environ.get('CONTAINERSHARE')
singularity_cache = os.environ.get('SINGULARITY_CACHEDIR', '%s/.singularity' %os.environ.get('HOME'))

if endpoint is None or containershare is None or singularity_cache is None:
    print('Please export ENDPOINT, CONTAINERSHARE, and SINGULARITY_CACHEDIR to the environment first!')
    sys.exit(1)

# Sanity check for the user

print('Endpoint: %s' %endpoint)
print('Containershare: %s' %containershare)
print('Singularity Cache: %s' %singularity_cache)

# Ensure containers are pulled to share

os.environ['SINGULARITY_PULLFOLDER'] = containershare
os.putenv('SINGULARITY_PULLFOLDER', containershare)

containers = requests.get(endpoint).json()

for container in containers:
    github = container['github'].split('/')[-2:]
    gh_pages = "https://%s.github.io/%s/tags.json" %(github[0], github[1])
    tags = requests.get(gh_pages).text.split('\n')
    for tag in tags:
        if tag:
            container_name = "docker://%s:%s" %(container['name'], tag)
            print(container_name)
            
            # Get the hash
            m = hashlib.md5()
            m.update(container_name.encode('utf-8'))
            container_hash = m.hexdigest()
            container_path = "%s/%s" %(containershare, container_hash)

            try:
                if not os.path.exists(container_path):
                    os.system('singularity pull --name %s.simg %s' %(container_hash, container_name))
            except:
                print('Error pulling %s' %container_name)
