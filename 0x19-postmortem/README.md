Postmortem: Server Outage on March 15, 2024


Issue Summary

Duration: The outage lasted from 10:30 AM to 12:15 PM on March 15, 2024.

Impact: The web application was unavailable for approximately 1 hour and 45 minutes. Users experienced 503 service unavailable errors. The outage affected 60% of our user base.

Root Cause: The root cause was a misconfiguration in the load balancer that led to all traffic being directed to a single server, which was unable to handle the load.

Timeline

•	10:30 AM : The issue was detected by our monitoring system, which alerted us to a sudden spike in server load and a drop in application availability.

•	10:35 AM : The on-call engineer began investigating the issue, starting with the application servers.

•	10:45 AM : The engineer noticed that one server was experiencing significantly higher load than the others. The assumption was made that this server was experiencing a hardware failure.

•	10:50 AM : The engineer attempted to restart the high-load server, but this did not resolve the issue.

•	11:00 AM : The incident was escalated to the infrastructure team for further investigation.

•	11:15 AM : The infrastructure team noticed the misconfiguration in the load balancer and corrected it.

•	12:00 PM : The application became available again as the load was distributed evenly across all servers.

Root Cause and Resolution

The root cause of the issue was a misconfiguration in the load balancer. This misconfiguration caused all traffic to be directed to a single server, which was unable to handle the load. This misconfiguration was introduced during a recent deployment, when a change was made to the load balancer configuration without proper testing.

The Issue was resolved by correcting the misconfiguration in the load balancer. This allowed traffic to be distributed evenly across all servers, which restored the application to full functionality.

Corrective and Preventative Measures

Things to Improve/Fix:

•	Improve our testing process to ensure that changes to the load balancer configuration are thoroughly tested before being deployed to production.

•	Implement a more robust monitoring system that can detect misconfigurations in the load balancer.

•	Improve our incident response process to ensure that incidents are escalated more quickly.

•	Implement tests on each server individually to ensure that any changes does not damage the server in anyway.

Tasks:

•	Update our testing process documentation to include steps for testing load balancer configurations.

•	Have a daily checklist to ensure that you have done each procedure correctly.

•	Implement additional monitoring on the load balancer to detect misconfigurations and additional monitoring to the primary and replica servers.

•	Review and update our incident response process to ensure that incidents are escalated more quickly.

0. https://drive.google.com/file/d/106PI5pPKXCBgBllDv_WC6-qtkpeyHC7T/view?usp=drivesdk

1. https://drive.google.com/file/d/10Ov6t3ZpP3fTy766gPgzhTAzWMas05Ku/view?usp=drivesdk

0. https://www.linkedin.com/posts/isabel-mothoa-672bb5204_alxengineering-activity-7195536217931710464-8VMK?utm_source=share&utm_medium=member_android

1. https://www.linkedin.com/posts/isabel-mothoa-672bb5204_alxengineering-activity-7195541364338520064-9x_g?utm_source=combined_share_message&utm_medium=member_android
