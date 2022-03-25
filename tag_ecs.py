import requests

iam = "https://iam.ru-moscow-1.hc.sbercloud.ru"
ecs = "https://ecs.ru-moscow-1.hc.sbercloud.ru"

def getToken(
    username,
    password,
    domain,
    project
):
    url = iam + "/v3/auth/tokens"
    headers = {
        "Content-Type": "application/json;charset=utf8"
    }
    data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": username,
                        "password": password,
                        "domain": {
                            "name": domain
                        }
                    }
                }
            },
            "scope": {
                "project": {
                    "id": project 
                }
            }
        }
    }
    request = requests.post(
        url,
        headers = headers,
        json = data
    ).json()
    return request

def tagEcs(
    token,
    projectId,
    ecsId
):
    url = ecs + "/v1/" + projectId + "/cloudservers/" + ecsId + "/tags/action"
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "X-Auth-Token": token
    }
    data = {
        "action": "create",
        "tags": [
            {
                "key": "test",
                "value": "test"
            },
            {
                "key": "test2",
                "value": "test2"
            }
        ]
    }
    request = requests.post(
        url,
        headers = headers,
        json = data
    )
    return request

iam_user = input("IAM Username: ")
password = input("IAM user password: ")
domain = input("Sbercloud Advanced account name: ")
project = input("Project ID: ")
ecsId = input("")

token = getToken(
    iam_user,
    password,
    domain,
    project
)

response = tagEcs(
    token,
    project,
    ecsId
)

print(response)