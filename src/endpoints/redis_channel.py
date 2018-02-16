import aioredis


async def get_redis(app):
    return await aioredis.create_redis(
        app['config']['redis_url'])


async def get_redis_pub_channel(app):
    app['pub_channel'] = await get_redis(app)


async def get_sub_channel(app, channel_name, redis=None):
    if not redis:
        redis = await get_redis(app)
    channel = await redis.subscribe(channel_name)
    return channel[0]
