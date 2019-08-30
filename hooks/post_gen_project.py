#!/usr/bin/env python

import logging

from json import loads
from os import getenv

try:
    from urllib.error import HTTPError
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import HTTPError, Request, urlopen
    from urllib import urlencode


DEFAULT_CHARACTER_ENCODING = 'UTF-8'


if __name__ == '__main__':
    vcs_type = 'github'
    username = 'mongodb-ansible-roles'
    project = '{{ cookiecutter.role_name }}'
    token = getenv('CIRCLECI_TOKEN', default='{{ cookiecutter.circleci_token }}')
    query = {'circle-token': token}
    params = urlencode(query)
    url = 'https://circleci.com/api/v1.1/project/{}/{}/{}/follow?{}'.format(
        vcs_type, username, project, params)
    request = Request(url)

    try:
        response = urlopen(request)
    except HTTPError:
        logging.error('failed to follow CircleCI project')

    body = response.read().decode(DEFAULT_CHARACTER_ENCODING)

    build_url = loads(body)['build_url']

    logging.info('followed project in CircleCI: {}'.format(build_url))
