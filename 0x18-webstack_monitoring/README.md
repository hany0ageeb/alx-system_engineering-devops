# 0x18. Webstack monitoring
![Monitoring](images/monitoring.png)
 ## Background context
 “You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

 Web stack monitoring can be broken down into 2 categories:
 - Application monitoring: getting data about your running software and making sure it is behaving as expected
 - Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

 ## Resources
 ### Read or watch:
 - [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
 - [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
 - [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
 - [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

 ## What is server monitoring?

 Organizations that depend on servers that are deployed in the cloud must implement server monitor solutions that help maintain the security of cloud servers while tracking their performance and availability. Server monitoring can have different objectives and track different key performance indicators (KPIs) based on the type of server, but the primary objective of server monitoring is always to protect the server from possible failure that would interrupt service availability.

 ## How does server monitoring work?

 The general process of server monitoring can be described in five steps:
 1. **Identify the most important KPIs:** server monitoring begins by identifying what data you want to track on each server. Your choices here depend on the server's functionality for your organization. For an application server, you might decide that the critical KPIs are availability and responsiveness. For a web server, capacity and speed might be the most important. For a data storage server, you might be more concerned about latency, data throughput, and data loss.

 2. **Set baseline KPI values:** once you have determined which KPIs are the most important, the next step is to measure the performance of each server on each KPI metric and determine an acceptable range of values for the KPI. This initial measurement will act as a baseline against which the future performance of the server will be measured.
 3. **Configure data collection and analysis:** a server monitoring tool must be appropriately configured to pull data from the servers deployed in your cloud environment. Server monitoring tools track the activity on the server by streaming event logs, also called log files, that the server automatically generates. Log files contain information about errors, user activity and security events that happen on the server. In addition to log files, server monitoring tools track server operating system KPIs including CPU and memory availability, network connectivity and disk performance.
 4. **Set up comprehensive and specific alerts:** now that you have configured your data collection and aggregation, the next step is to build out an alert system that will send notifications to you and your team when there is a KPI breach and your chosen metrics drop below threshold levels.