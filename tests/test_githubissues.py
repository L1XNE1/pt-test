import pytest
import json
import responses
from src.githubissues import GitHubIssues


@responses.activate
def test_get_list_of_repos():
    with open('tests/data/devopshq_list_of_repos.json', 'r') as f:
        test_input = f.read()

    responses.get(
        'https://api.github.com/orgs/devopshq/repos',
        json=json.loads(test_input),
    )

    g = GitHubIssues('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')
    output = g.get_list_of_repos('devopshq')

    expected_output = [
        'crosspm',
        'vspheretools',
        'zabbix-youtrack-action'
    ]

    bad_output = [
        '1crosspm',
        'vs2pheretools',
        'zabb3ix-youtrack-action'
    ]

    output.sort()
    expected_output.sort()
    bad_output.sort()

    assert output == expected_output
    assert output != bad_output
