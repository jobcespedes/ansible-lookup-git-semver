# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
        lookup: git_semver
        author: Job Céspedes <jobcespedes@gmail.com>
        version_added: "2.9"
        short_description: get/bump version from git current branch latest tag
        requirements:
            - semantic_version
        description:
            - This lookup returns/bump the version from git current branch latest tag
        options:
            _terms:
                description: path of repo
                required: True
            bump:
                description:
                    - increase# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
        lookup: git_semver
        author: Job Céspedes <jobcespedes@gmail.com>
        version_added: "2.9"
        short_description: get/bump version from git current branch latest tag
        requirements:
            - semantic_version
        description:
            - This lookup returns/bump the version from git current branch latest tag
        options:
            _terms:
                description: path of repo
                required: True
            bump:
                description:
                    - increase/bump version number: major, minor, patch
                default: ''
                type: string
                required: False
                choices: ['major', 'minor', 'patch']
"""

EXAMPLES = """
- vars:
    version: "{{ lookup('git_semver', playbook_dir) }}"
    next_patch_version: "{{ lookup('git_semver', playbook_dir, bump='patch') }}"
    next_minor_version: "{{ lookup('git_semver', playbook_dir, bump='minor') }}"
    next_major_version: "{{ lookup('git_semver', playbook_dir, bump='major') }}"
"""

RETURN = """
_raw:
  description:
    - version from git current branch latest tag
"""
import semantic_version
import git
from git import Repo
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        bump = kwargs.get('bump', '').lower()
        if not isinstance(bump, string_types) or bump not in ['patch', 'minor', 'major', '']:
            raise AnsibleError('"bump" must be a string and one of "patch", "minor" or "major", not %s' % bump)

        ret = []
        for term in terms:
            display.debug("Repo path: %s" % term)
            repo = Repo(term)

            display.vvvv(u"Git semver lookup using %s as repo" % repo)
            try:
                if repo:
                    # Check this is a git repo
                    assert not repo.bare

                    # Get tag
                    version = repo.git.describe('--tags', '--abbrev=0')

                    # Validate semver
                    if not semantic_version.validate(version):
                        raise AnsibleError('Tag "%s" is not a proper semantic version' % version)

                    # bump
                    if bump:
                        semver = semantic_version.Version(version)
                        version = getattr(semver, 'next_'+ bump)()

                    # return
                    ret.append(version)
                else:
                    raise AnsibleParserError()
            except AnsibleParserError:
                raise AnsibleError("could not get version in lookup: %s" % term)

        return ret
/bump version number: major, minor, patch
                default: ''
                type: string
                required: False
                choices: ['major', 'minor', 'patch']
"""

EXAMPLES = """
- vars:
    version: "{{ lookup('git_semver', playbook_dir) }}"
    next_patch_version: "{{ lookup('git_semver', playbook_dir, bump='patch') }}"
    next_minor_version: "{{ lookup('git_semver', playbook_dir, bump='minor') }}"
    next_major_version: "{{ lookup('git_semver', playbook_dir, bump='major') }}"
"""

RETURN = """
_raw:
  description:
    - version from git current branch latest tag
"""
import semantic_version
import git
from git import Repo
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        bump = kwargs.get('bump', '').lower()
        if not isinstance(bump, string_types) or bump not in ['patch', 'minor', 'major', '']:
            raise AnsibleError('"bump" must be a string and one of "patch", "minor" or "major", not %s' % bump)

        ret = []
        for term in terms:
            display.debug("Repo path: %s" % term)
            repo = Repo(term)

            display.vvvv(u"Git semver lookup using %s as repo" % repo)
            try:
                if repo:
                    # Check this is a git repo
                    assert not repo.bare

                    # Get tag
                    version = repo.git.describe('--tags', '--abbrev=0')

                    # Validate semver
                    if not semantic_version.validate(version):
                        raise AnsibleError('Tag "%s" is not a proper semantic version' % version)

                    # bump
                    if bump:
                        semver = semantic_version.Version(version)
                        version = getattr(semver, 'next_'+ bump)()

                    # return
                    ret.append(version)
                else:
                    raise AnsibleParserError()
            except AnsibleParserError:
                raise AnsibleError("could not get version in lookup: %s" % term)

        return ret
