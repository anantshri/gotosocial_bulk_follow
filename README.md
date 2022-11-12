# GOTOSOCIAL BULK FOLLOW Option

This script provides a quick bulk follow option for the gotosocial server

Provide your auth token and instance name in either the code or as commandline arguments

## Why was this created

toot cli is one the good options however the api of gotosocial works slightly different then what tootcli looks for and hence toot follow command doesn't works. hence the script


## NOTE ABOUT AUTH TOKEN

1. Simplest way to get auth token is to use tootcli and try to authenticate. Check the inspect console for the exact token value and use it in the tootcli.

2. Alterantively folowing two api calls can be made to get a token code for yourself

a. We need to register our app
```
curl -X 'POST' \
  'https://example.org/api/v1/apps' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d 'client_name=bulk_follow&redirect_uris=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scopes=follow'
```

b. We need to get the token which can be obtained by going to 

here client_ID is in the response of first request

`https://example.org/oauth/authorize/?response_type=code&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=read+write+follow&client_id=<client_ID>`

Note: I have had mixed responses with the second method

