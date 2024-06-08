Issue Summary
Duration of the Outage:

Start: June 1, 2024, 14:30 UTC
End: June 1, 2024, 16:00 UTC
Impact:

The main web application was slow and intermittently unavailable.
Users experienced 504 Gateway Timeout errors.
Approximately 80% of users were affected.
Root Cause:

A misconfiguration in the database connection pool settings led to resource exhaustion under peak load conditions.
Timeline
14:30 - Issue detected via monitoring alert indicating increased response times and error rates.
14:35 - Engineers noticed 504 errors and began investigating the web server logs.
14:45 - Assumed root cause was a potential network issue; network team was notified.
15:00 - Network checks returned normal, focus shifted to the application layer.
15:10 - Suspected a recent deployment; rollback initiated but no improvement.
15:25 - Database team identified high connection counts and lock contention.
15:30 - Misleading debugging path: Investigated potential database corruption.
15:45 - Incident escalated to the database admin team.
15:50 - Root cause identified: Misconfigured database connection pool.
15:55 - Connection pool settings adjusted.
16:00 - System restored to normal operation.
Root Cause and Resolution
Root Cause:

The database connection pool was configured with an insufficient maximum limit of connections. Under peak load, this caused threads to wait for available connections, leading to high latency and eventual timeouts.
Resolution:

The connection pool settings were updated to increase the maximum number of connections and to better match the application’s load requirements. This change was applied and tested, resulting in the immediate restoration of normal service.
Corrective and Preventative Measures
Improvements:

Review and optimize database connection pool configurations based on load testing data.
Implement automated monitoring and alerts for connection pool utilization.
Conduct regular load testing to anticipate and prepare for peak usage scenarios.
Tasks:

Patch Nginx Server: Update Nginx configuration to handle high loads more effectively.
Add Monitoring: Implement monitoring on server memory and connection pool metrics.
Conduct Training: Educate the development team on best practices for configuring connection pools.
Regular Load Testing: Schedule quarterly load tests to ensure the system can handle peak traffic.
Update Documentation: Document the new connection pool settings and the rationale for their values.
Review Incident Response Plan: Refine the incident response plan to ensure quicker identification of similar issues.
By addressing these areas, we can prevent similar outages in the future and ensure a more robust and resilient web application infrastructure.