# git_semver
Ansible lookup plugin that returns/bumps the version from git current branch latest tag

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
    version: "{{ lookup('git_semver', playbook_dir) }}"
    next_patch_version: "{{ lookup('git_semver', playbook_dir, bump='patch') }}"
    next_minor_version: "{{ lookup('git_semver', playbook_dir, bump='minor') }}"
    next_major_version: "{{ lookup('git_semver', playbook_dir, bump='major') }}"
  debug:
     msg: |
        {{version}}
        {{next_patch_version}}
        {{next_minor_version}}
        {{next_major_version}}
```
