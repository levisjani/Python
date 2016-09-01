python
rom slackclient import SlackClient
slack_client = SlackClient('your test token here')
slack_client.api_call("api.test")
slack_client.api_call("auth.test")
