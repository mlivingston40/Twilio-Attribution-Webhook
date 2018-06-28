# Twilio Attribution

### General Steps To Deploy On AWS Lambda

1) Everything in source boundle has to be at root level
-- This even means all 3rd party packages 
in venv/lib/python3.6/site-packages will need to be moved too

2) Zip everything up  

```
 zip -r9 ~/deploy_bundle.zip .
```

From Here uploading to the AWS lambda console is pretty straight forward, one thing to keep 
in mind is if you have an 3rd party packages compiled in C, they have to pre-compiled (like Pandas and Numpy)

 ### AWS API Gateway
 1) We will want to create an API Post here to direct our Twilio Number to 
 
 ### Webhook HTTP POST setting
 1)  Next, we will take the URL we created above and put it in the Twilio console for our number 
 "A Call Comes IN" - Webhook.  Then our AWS lambda function will fire when the number is called 