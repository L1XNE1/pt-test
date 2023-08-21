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


try:
    token = os.environ['GITHUB_TOKEN']
except KeyError:
    print('Ошибка! Переменная GITHUB_TOKEN пуста.')
    raise SystemExit(1)

orgname = 'devopshq'

g = GitHubIssues(token)
print_issues_of_org(g.get_issues_of_org(orgname))


#тут одна функция, которая выводит список так как указано на скриншоте в тестовом задании
