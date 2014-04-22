# coding=utf-8
import werobot


robot = werobot.WeRoBot(token='myyunfan')  # 填写你的token


# 被用户关注
@robot.subscribe
def subscribe(message):
    return 'Hello My Friend!'


from werobot.reply import ArticlesReply, Article


@robot.text
def echo(message):
    myreply = ArticlesReply(message=message)
    article = Article(
        title="WeRoBot",
        description="WeRoBot是一个微信机器人框架",
        img="https://github.com/apple-touch-icon-144.png",
        url="https://github.com/whtsky/WeRoBot"
        )
    myreply.add_article(article)
    if message.content == 'a':
        return myreply
    return message.content


@robot.image
def getImage(message):
    return message.img


@robot.location
def getLocation(message):
    # Do what you love to do
    return message.label


# 只有之前的都没有匹配，handler最后被调用
@robot.handler
def hello(message):
    return 'Hello World!'


robot.run()
