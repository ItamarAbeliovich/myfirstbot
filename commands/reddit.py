import requests
import logutil

logger = logutil.get_logger(__name__, 'log.txt')

async def get_post(bot, *args):
    if not len(args):
        return await bot.say('Usage: `!reddit <subreddit-name> <OPTIONAL: name of post>`\n'
                             'Gets the top post from a sub or finds one of the top posts by keyword.')

    logger.debug('Fetching posts from reddit')

    url = 'http://reddit.com/r/%s/top/.json' % args[0]
    if len(args) >= 2:
        url = 'http://reddit.com/r/%s/search.json?q=%s&sort=top&restrict_sr=true' % (args[0], ' '.join(args[1:]))

    res = requests.get(url, headers={'User-Agent': 'The President bot v0.1'})
    if not res:
        logger.error('While fetching posts from r/%s: error %s' %
                     (args[0], res.status_code))
        return await bot.say('Error fetching post')

    json = res.json()
    posts = list(filter(lambda post: not post['over_18'],
                        map(lambda post: post['data'], json['data']['children'])))

    logger.debug('Reddit posts fetched')
    if not len(posts):
        logger.debug('No posts found')
        return await bot.say('Post not found')

    # if len(args) >= 2:
    #     logger.debug('Finding post by keyword')
    #     keyword = ' '.join(args[1:])
    #     post = next((i for i in posts if keyword in i['title']), None)
    #     if post is None:
    #         logger.debug('No posts found with the specified keyword: %s' % keyword)
    #         return await bot.say('Post not found')
    #     logger.debug('Found matching post')
    #     return await bot.say(post['url'])

    logger.debug('Returning top post from %s' % args[0])
    return await bot.say(posts[0]['url'])
