import requests
from datetime import datetime, timedelta

TOP_SIZE = 20 # A number of the best repositories
TIME_PERIOD = 7 # Days

def get_starting_date(time_period):
    return (datetime.today() - timedelta(days=time_period)).strftime("%Y-%m-%d")

def get_trending_repositories(top_size, time_period):
    request = \
    requests.get('https://api.github.com/search/repositories?q=created:>%s&sort=stars&per_page=%d'
        % (get_starting_date(time_period), top_size))
    return request.json()["items"]

if __name__ == '__main__':
    print("%d best repositories on https://github.com for last %d days:"
        % (TOP_SIZE, TIME_PERIOD))

    for repository in get_trending_repositories(TOP_SIZE, TIME_PERIOD):
        print("Repository name: %s\nLink: %s\nOpen issues amount: %s\n" 
            % (repository["name"], 
                repository["html_url"], 
                repository["open_issues"]))