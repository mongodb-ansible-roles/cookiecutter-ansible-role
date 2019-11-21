Ansible role for {{ cookiecutter.role_name }}
==================================

{{ cookiecutter.role_description }}

[![CircleCI](https://img.shields.io/circleci/build/github/{{ cookiecutter.github_username }}/ansible-role-{{ cookiecutter.role_name }}/master?style=flat-square)](https://circleci.com/gh/{{ cookiecutter.github_username }}/ansible-role-{{ cookiecutter.role_name }})

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| name | desc | type | default | required |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-{{ cookiecutter.role_name }}
      vars:
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
