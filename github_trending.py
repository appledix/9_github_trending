import requests
from datetime import datetime, timedelta

SIZE_OF_THE_REPOSITORY_TOP = 20
TIME_PERIOD = 7

def get_starting_date(time_period):
    return (datetime.today() - timedelta(days=time_period)).strftime("%Y-%m-%d")

def get_trending_repositories(top_size, time_period):
    payload = {'q':'created:>{}'.format(get_starting_date(time_period)),
                'sort':'stars',
                'per_page':top_size}
    request = \
    requests.get('https://api.github.com/search/repositories', params=payload)
    return request.json()["items"]

if __name__ == '__main__':
    print("{} best repositories on https://github.com for last {} days:".format(
        SIZE_OF_THE_REPOSITORY_TOP,
        TIME_PERIOD))

    for repository in get_trending_repositories(SIZE_OF_THE_REPOSITORY_TOP, TIME_PERIOD):
        print("Repository name: {}\nLink: {}\nOpen issues amount: {}\n".format(
            repository["name"],
            repository["html_url"],
            repository["open_issues"]))