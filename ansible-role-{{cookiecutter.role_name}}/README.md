Ansible role for {{ cookiecutter.role_name }}
==================================

{{ cookiecutter.role_description }}

[![GitHub Actions](https://github.com/{{ cookiecutter.github_username }}/ansible-role-{{ cookiecutter.role_name }}/workflows/Molecule%20Test/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.role_name }}/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/{{ cookiecutter.github_username }}/ansible-role-{{ cookiecutter.role_name }}/workflows/Release/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.role_name }}/actions?query=workflow%3A%22Molecule+Test%22)

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
```

License
-------

[Apache License](LICENSE)
