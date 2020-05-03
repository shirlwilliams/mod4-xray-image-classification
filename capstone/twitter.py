import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='GY5V48tnTfsLMstmdEbNv1dMU',
                        consumer_secret='z8c7ud6BnwXC8mPnsMeMa2qWDP26Ir5ty4XbqVQDbccPclBUM0',
                        access_token_key='YOUR_ACCESS_TOKEN_KEY',
                        access_token_secret='YOUR_ACCESS_TOKEN_SECRET')

# test authentication
print(twitter_api.VerifyCredentials())
