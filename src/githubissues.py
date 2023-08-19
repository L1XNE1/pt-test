import requests


class GitHubIssues:
    baseurl = 'https://api.github.com' #поле (переменная) класса

    def __init__(self, token):   #конструктор класса, который позволяет инициализировать
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def get_list_of_repos(self, owner):  #обращается к апи гитхаба и запрашивает список репозиториев указанного пользователя (организации)
        url = f'{self.baseurl}/orgs/{owner}/repos'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise SystemExit('Ошибка')

        repos = [] #инициализируется пустой список в переменной repos.
        for f in response.json():
            repo_name = f['name']
            repos.append(repo_name)

        return repos

    def get_issues_of_repo(self, owner, name): #запрашивает список issues у репозитория
        url = f'{self.baseurl}/repos/{owner}/{name}/issues'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise SystemExit('Ошибка')

        issues = [] #инициализируется пустой список в переменной issues
        for issue in response.json():
            issue_number = issue['number']
            issue_title = issue['title']

            issues.append(f'{issue_number}: {issue_title}')

        return issues

    def get_issues_of_org(self, org): #функция которая объединяет функции предыдущих двух функций.
        repos = self.get_list_of_repos(org)
        issues = []
        for repo in repos: #для каждого репозитория из списка репозиториев добавляем в список issues словарь, который хранит имя репозитория и список issues.
            issues.append({
                'repo': repo,
                'issues': self.get_issues_of_repo(org, repo)
            })

        return issues

### тут написан класс со всеми функциями.
