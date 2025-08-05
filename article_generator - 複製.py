mport requests

def post_to_pixnet(article):
    url = "https://emma.pixnet.cc/blog/articles"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    data = {
        "title": article["title"],
        "body": article["content"],
        "status": "publish"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()