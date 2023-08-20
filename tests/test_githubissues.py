import pytest
import json
import responses
from src.githubissues import GitHubIssues
#каждая функция ниже это отдельный тест

@responses.activate #подделываем ответы для модуля requests (офлайн тест)
def test_get_list_of_repos():
    with open('tests/data/devopshq-repos.json', 'r') as f: #читает файл с тестовыми данными
        test_input = f.read()

    responses.get( # подделываем get запрос
        'https://api.github.com/orgs/devopshq/repos',
        json=json.loads(test_input),
    )

    g = GitHubIssues('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')
    output = g.get_list_of_repos('devopshq') #результат это список 

    expected_output = [ # тут руками написано что ждем
        'crosspm',
        'vspheretools',
        'zabbix-youtrack-action'
    ]

    bad_output = [
        '1crosspm',
        'vs2pheretools',
        'zabb3ix-youtrack-action'
    ]

    #ниже сортируются все списки
    output.sort()
    expected_output.sort()
    bad_output.sort()

    assert output == expected_output #мы ждем что output должен быть равен тому, что мы ждем (выше)
    assert output != bad_output


@responses.activate
def test_get_issues_of_repo():
    with open('tests/data/devopshq-crosspm-issues.json', 'r') as f:
        test_input = f.read()

    responses.get(
        'https://api.github.com/repos/devopshq/crosspm/issues',
        json=json.loads(test_input),
    )

    g = GitHubIssues('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')
    output = g.get_issues_of_repo('devopshq', 'crosspm')

    expected_output = [
        '123: Altsearch',
        '122: [pre-commit.ci] pre-commit autoupdate'
    ]

    output.sort()
    expected_output.sort()

    assert output == expected_output


@responses.activate #4 разных запроса (подделывает на 4 разных запроса)
def test_get_issues_of_org():
    with open('tests/data/devopshq-repos.json', 'r') as f:
        test_input = f.read()
    responses.get(
        'https://api.github.com/orgs/devopshq/repos',
        json=json.loads(test_input),
    )

    with open('tests/data/devopshq-crosspm-issues.json', 'r') as f:
        test_input_crosspm = f.read()
    responses.get(
        'https://api.github.com/repos/devopshq/crosspm/issues',
        json=json.loads(test_input_crosspm),
    )

    with open('tests/data/devopshq-vspheretools-issues.json', 'r') as f:
        test_input_vspheretools = f.read()
    responses.get(
        'https://api.github.com/repos/devopshq/vspheretools/issues',
        json=json.loads(test_input_vspheretools),
    )

    with open('tests/data/devopshq-zabbix-youtrack-action-issues.json', 'r') as f:
        test_input_zabbix = f.read()
    responses.get(
        'https://api.github.com/repos/devopshq/zabbix-youtrack-action/issues',
        json=json.loads(test_input_zabbix),
    )

    g = GitHubIssues('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')
    output = g.get_issues_of_org('devopshq')

    expected_output = [ #ожидаемый вывод написан руками
        {
            'repo': 'crosspm',
            'issues': [
                '123: Altsearch',
                '122: [pre-commit.ci] pre-commit autoupdate'
            ]
        },
        {
            'repo': 'vspheretools',
            'issues': [
                '9: fail Travis build if tests fail'
            ]
        },
        {
            'repo': 'zabbix-youtrack-action',
            'issues': [
                '3: Create install script',
                '2: Create good docs',
                '1: Refactor code'
            ]
        }
    ]

    assert output == expected_output #сравниваем что мы получили с ожидаемым выводом

