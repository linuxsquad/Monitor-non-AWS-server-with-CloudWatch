# Monitor-non-AWS-server-with-CloudWatch

CloudWatch is collection of monitoring tools for AWS resources: EC2, S3, etc.. 

However, you can use CloudWatch to monitor your non-AWS (external, on-premise) resources. 

Here are simple steps: 

#. Create an account on AWS and obtain credentials (ID and key) for at least one user with permissions to use CloudWatch
#. Enable CloudWatch 
#. Install CloudWatch agent on your server 
   http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html

#. You can test it by letting it to ship /var/log/messages or other log files to CloudWatch
5- You can modify included Python script for monitoring your favorite server or application parameters. This particular one ship percentage of free memory and number of active HTTPD processes in JSON format to AWS CloudWatch. 
6- Go back to CloudWatch and create Metric filter/s
7- Convert the filters into CloudWatch dashboard graphs. 
8- Cloudwatch comes with Alarms that can notify your based on pre-set values and conditions.

