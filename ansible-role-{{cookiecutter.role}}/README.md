Ansible role for {{ cookiecutter.role }}
==================================

{{ cookiecutter.role_description }}

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-{{ cookiecutter.role }}/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles)

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
    - role: ansible-role-{{ cookiecutter.role }}
      vars:
```

License
-------

[Apache License](LICENSE)
