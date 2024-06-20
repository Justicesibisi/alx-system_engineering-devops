0x19. Postmortem

#TASK 1
Postmortem Report for NJ Sibisi Co.
Issue Summary
Duration of the Outage:
Start Time: June 5, 2024, 5:00 PM (SAST)
End Time: June 5, 2024, 8:00 PM (SAST)
Impact:
The outage caused the primary e-commerce service to be unavailable. Users were unable to browse products or complete purchases. Approximately 85% of users were affected, leading to a significant loss in potential revenue and a surge in customer complaints.
Root Cause:
A sudden spike in traffic due to a promotional event overwhelmed the database server, causing it to crash. The auto-scaling mechanism failed to trigger due to a misconfiguration in the threshold settings.
Timeline
5:00 PM: Issue detected via monitoring alerts indicating high latency and timeouts.
5:05 PM: On-call engineer received the alert and began investigation.
5:10 PM: Initial assumption was a network issue; network logs were checked.
5:20 PM: Network issue ruled out; focus shifted to server resources.
5:30 PM: Database server found to be unresponsive; checked server metrics.
5:45 PM: Misleading path: suspected a DDoS attack, implemented preliminary mitigations.
6:00 PM: Escalated to the database administration team.
6:15 PM: Root cause identified as a traffic spike; checked auto-scaling configuration.
6:30 PM: Discovered misconfiguration in auto-scaling thresholds.
7:00 PM: Correct configuration applied; auto-scaling triggered.
7:30 PM: Database server scaled up; service began to recover.
8:00 PM: Service fully restored; monitoring confirmed stability.
Root Cause and Resolution
Root Cause:
The database server was overwhelmed by a traffic spike due to a promotional event. The auto-scaling mechanism designed to handle such spikes failed to activate because the threshold for triggering the auto-scaling was set too high.
Resolution:
The misconfiguration in the auto-scaling threshold was corrected. The correct threshold settings were applied, which allowed the auto-scaling feature to activate promptly. Additional database instances were launched to handle the increased load, and the system recovered.
Corrective and Preventative Measures
Improvements:
Review and adjust auto-scaling configurations to ensure they are set appropriately for expected traffic volumes.
Implement additional monitoring to detect traffic spikes earlier and trigger alerts before systems reach critical load.
Conduct regular load testing to ensure the system can handle promotional events and similar high-traffic scenarios.
TODO List:
Patch Auto-Scaling Configuration: Verify and adjust all auto-scaling thresholds across services to appropriate levels.
Enhance Monitoring: Add monitoring for traffic spikes and resource usage with alert thresholds set well before critical levels.
Load Testing: Schedule regular load testing, especially before major promotional events, to ensure systems can handle anticipated traffic.
Documentation and Training: Update documentation on handling traffic spikes and auto-scaling configurations. Train the team on these updates to ensure everyone is aware of the procedures and configurations.
Review Incident Response Procedures: Analyze the current incident response plan to identify areas for improvement and ensure a quicker resolution in future incidents.
By implementing these measures, NJ Sibisi Co. aims to prevent similar outages in the future, ensuring better service reliability and customer satisfaction.


#TASK 2
Postmortem Report for NJ Sibisi Co.
The Great Traffic Spike Incident of 2024
Issue Summary
Duration of the Outage:
Start Time: June 5, 2024, 5:00 PM (SAST)
End Time: June 5, 2024, 8:00 PM (SAST)
Impact:
Imagine walking into your favorite store and finding the doors locked with a sign that says, "Come back later!" That's what happened to 85% of our users. Our e-commerce service took an unexpected siesta, preventing users from browsing products or completing purchases. Cue the dramatic music and customer complaints.
Root Cause:
A promotional event spiked traffic like a three-pointer at the buzzer, overwhelming our database server. The auto-scaling mechanism was like a deer in headlights, thanks to a misconfiguration in the threshold settings.
Timeline
5:00 PM:  Issue detected via monitoring alerts showing high latency and timeouts.
5:05 PM:  On-call engineer received the alert and started the investigation.
5:10 PM:  Assumed a network issue; checked network logs.
5:20 PM:  Network issue ruled out; focus shifted to server resources.
5:30 PM:  Database server found to be unresponsive; checked server metrics.
5:45 PM:  Misleading path: suspected a DDoS attack, implemented preliminary mitigations.
6:00 PM:  Escalated to the database administration team.
6:15 PM:  Root cause identified as a traffic spike; checked auto-scaling configuration.
6:30 PM:  Discovered misconfiguration in auto-scaling thresholds.
7:00 PM:  Correct configuration applied; auto-scaling triggered.
7:30 PM:  Database server scaled up; service began to recover.
8:00 PM:  Service fully restored; monitoring confirmed stability.
Root Cause and Resolution
Root Cause:
The database server was overwhelmed by a traffic spike due to a promotional event. The auto-scaling mechanism designed to handle such spikes failed to activate because the threshold for triggering the auto-scaling was set too high.
Resolution:
We rolled up our sleeves, adjusted the misconfiguration in the auto-scaling threshold, and voila! The correct settings were applied, the auto-scaling feature kicked in, and additional database instances were launched to handle the load. Crisis averted.
Corrective and Preventative Measures
Improvements:
Auto-Scaling Configurations: Regularly review and adjust auto-scaling configurations to match expected traffic.
Enhanced Monitoring: Implement additional monitoring to detect traffic spikes early and trigger alerts before systems hit critical load.
Regular Load Testing: Conduct load testing, especially before promotional events, to ensure systems can handle the expected traffic.
TODO List:
Patch Auto-Scaling Configuration: Verify and adjust all auto-scaling thresholds across services to appropriate levels.
Enhance Monitoring: Add monitoring for traffic spikes and resource usage with alert thresholds set well before critical levels.
Load Testing: Schedule regular load testing, particularly before major promotional events, to ensure systems can handle anticipated traffic.
Documentation and Training: Update documentation on handling traffic spikes and auto-scaling configurations. Train the team on these updates to ensure everyone is aware of the procedures and configurations.
Review Incident Response Procedures: Analyze the current incident response plan to identify areas for improvement and ensure a quicker resolution in future incidents.
By implementing these measures, NJ Sibisi Co. aims to prevent similar outages in the future, ensuring better service reliability and customer satisfaction.

"""Remarks 
Remember, folks: failing is fine, but failing twice because of the same issue is not. Let's learn from this and keep our systems running smoothly! 
"""
