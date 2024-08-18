
Postmortem Report: Web Service Outage - August 14, 2024

Issue Summary Duration: The outage lasted for 2 hours and 45 minutes, from 2:15 PM to 5:00 PM UTC on August 14, 2024.

Impact: During the outage, our main web application became inaccessible to 85% of users. The remaining 15% experienced significantly slow loading times and intermittent errors when trying to perform critical actions such as logging in or accessing their dashboards. Approximately 45,000 users were directly impacted by the downtime, resulting in a surge of customer support inquiries and a noticeable drop in service reliability metrics.

Root Cause: The root cause of the outage was a misconfiguration in the load balancer settings, which was inadvertently triggered during a routine deployment. The misconfiguration caused the load balancer to route traffic to an offline server cluster, leading to the service disruption.

Timeline 2:15 PM UTC: The issue was first detected by automated monitoring systems, which flagged a significant drop in successful HTTP requests and a spike in response times.

2:20 PM UTC: The on-call engineer received an alert and began investigating the issue, starting with checking the application servers for any signs of failure or high load.

2:30 PM UTC: Initial investigations suggested that the issue might be related to a sudden increase in traffic, leading the team to focus on scaling up resources in the web server tier.

2:45 PM UTC: The incident was escalated to the network engineering team after it became clear that resource scaling was not resolving the issue.

3:00 PM UTC: The network team identified that a deployment had been made just before the outage began. The team started reviewing the deployment logs and configuration changes.

3:30 PM UTC: Misleading data in the logs suggested that a database issue might be at fault, leading to additional time spent investigating database performance and connectivity.

4:15 PM UTC: After further analysis, the network team discovered the load balancer misconfiguration and began working to revert the changes.

4:45 PM UTC: The misconfiguration was corrected, and the application started to recover gradually as traffic was routed correctly.

5:00 PM UTC: Full service was restored, and all systems were confirmed to be functioning normally.

Root Cause and Resolution Root Cause: The root cause of the outage was traced to a change in the load balancer configuration that was part of a routine deployment. The new configuration incorrectly routed traffic to a server cluster that had been decommissioned but not fully removed from the load balancer's pool. As a result, the majority of incoming traffic was directed to non-existent servers, leading to failed requests and timeouts.

Resolution: The resolution involved reverting the load balancer configuration to its previous state, removing the decommissioned server cluster from the load balancer's settings, and performing a full restart of the affected services. Once these changes were applied, traffic was routed correctly, and the application recovered fully.

Corrective and Preventative Measures Improvements:

Configuration Management: Improve the configuration management process to include stricter validation checks before deployment, particularly for critical components like the load balancer. Decommissioning Process: Enhance the server decommissioning process to ensure all references to decommissioned resources are removed from active configurations. Monitoring and Alerts: Implement more granular monitoring of load balancer traffic and health checks to catch similar issues more quickly. Task List:

Implement a validation script to automatically check for any inactive or offline server references in load balancer configurations before deployment. Update the decommissioning checklist to include steps for removing all related configurations from active components. Deploy additional monitoring for load balancer health, focusing on traffic routing and server availability. Conduct a post-incident review training session for the engineering team to cover lessons learned and improve response strategies for future incidents.
