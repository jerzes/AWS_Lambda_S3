# Lambda function description
This function is triggered when file has been  upploaded to S3 bucket.
Base on this event is created new file ```report.log``` and put to it filename of uploaded object into S3.
Finally report.log file is uploaded to S3.
