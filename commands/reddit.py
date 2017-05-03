import requests

async def get_post(bot, *args):
    if not len(args):
        return await bot.say('Usage: `!reddit <subreddit-name> <OPTIONAL: name of post>`\n'
                             'Gets the top post from a sub or finds one of the top posts by keyword.')

    res = requests.get('http://reddit.com/r/%s/top/.json')
    posts = list(filter(lambda post: not post['over_18'],
                        map(lambda post: post['data'], res.json()['data']['children'])))

    if not len(posts):
        return await bot.say('Post not found')

    if len(args) >= 2:
        keyword = ' '.join(args[1:])
        post = next((i for i in posts if keyword in i['title']), None);
        if post is None:
            return await bot.say('Post not found');
        return await bot.say(post['url'])

    return await bot.say(posts[0]['url'])