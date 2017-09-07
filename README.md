# Monitor-non-AWS-server-with-CloudWatch

CloudWatch is collection of monitoring tools for AWS resources: EC2, S3, etc.. 

However, you can use CloudWatch to monitor your non-AWS (external, on-premise) resources. 

Here are simple steps: 

1. Create an account on AWS and obtain credentials (ID and key) for at least one user with permissions to use CloudWatch
1. Enable CloudWatch 
1. Install AWS Command Line Interface for your OS
   http://docs.aws.amazon.com/cli/latest/userguide/installing.html
1. The supplied Python script monitors CPU times (idle, user, sys, steal) and percentage of the free memory. In addition, it will count number of processes that match a name that you have to specify. In our case, we are interested in HTTPD. 
1. Start the script in background mode
  # nohup monitor_RAM_HTTP.py &
1. Go back to CloudWatch and after couple minutes, check Metrics->Custom Namespaces. You should notice a new box. 
1. Click on the box with matching name to review new metrics (CPU, RAM, HTTPD. etc).
1. Cloudwatch comes Graph and Alarms that you can setup using your metics. 

Note: We upload metrics directly to CloudWatch bypassing intemittent step of logging them first and then processing the logs. That's why you won't fine any corresponding log files under Logs section. But you still can review raw data for the uploaded metrics.
