import os
from githubissues import GitHubIssues


def print_issues_of_org(issues_dict):
    for issue in issues_dict:
        repo = issue['repo']
        print(repo + ':\n')

        issues = issue['issues']
        for i in issues:
            print('  ' + i)
        print()


#token = os.environ['GITHUB_TOKEN']
#with open('/run/secrets/github-token', 'r') as f:
#    token = f.read()
token = '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'

orgname = 'devopshq'

g = GitHubIssues(token)
print_issues_of_org(g.get_issues_of_org(orgname))


#тут одна функция, которая выводит список так как указано на скриншоте в тестовом задании
