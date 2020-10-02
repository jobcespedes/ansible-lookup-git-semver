# git_semver
Ansible lookup plugin that returns/bumps the version from git latest branch tag. Optionally, it could return tag's branch and commit

## Requirements
- python git
- python semantic-version

## Install
Drop it in the respective directory
> You can activate a custom lookup by either dropping it into a lookup_plugins directory adjacent to your play, inside the plugins/lookup/ directory of a collection you have installed, inside a standalone role, or in one of the lookup directory sources configured in ansible.cfg

[From Ansible docs](https://docs.ansible.com/ansible/latest/plugins/lookup.html#enabling-lookup-plugins)

## Example
```yaml
- vars:
    version: "{{ lookup('git_semver', playbook_dir') }}"
    version_next_patch: "{{ lookup('git_semver', playbook_dir, bump='patch') }}"
    version_next_minor: "{{ lookup('git_semver', playbook_dir, bump='minor') }}"
    version_next_major: "{{ lookup('git_semver', playbook_dir, bump='major') }}"
    version_list: "{{ lookup('git_semver', playbook_dir, want='list') }}"
    version_dict: "{{ lookup('git_semver', playbook_dir, want='dict') }}"
  debug:
    msg:  |
      {{ version }}
      {{ version_next_patch }}
      {{ version_next_minor }}
      {{ version_next_major }}
      {{ version_list }}
      {{ version_dict}}
```
