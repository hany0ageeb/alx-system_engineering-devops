# What happens when you type [google.com](https://www.google.com) in your browser and press Enter

Each device on the Internet - servers, cell phones, etc - all have a unique address called IP address.

Your browser need the IP address of the server that maps to google.com in order to connect with it.

Domain Name System (DNS) resolves domain names to their IP addresses.

## What is Domain Name Resolution?

Domain Name Resolution is a translation process between the domain name that people use while writing in their browsers and the site's IP (Internet Protocol) address.

## How Domain Name Resolution Work?

The DNS Resolution process starts when the user types a URL address on the browser and hits Enter. At this point, the browser asks the operating system for a specific page, in this case google.com.

Since the Operating System does not know where "www.google.com" is, it queries a DNS resolver. The query the OS sends to the DNS resolver has a special flag that tells it is a "recursive query". This means that the resolver must complete the recursion and the response must be either an IP address or an error.

For most users, their DNS resolver is provided by their Internet Service Provider (ISP), or they are using an open source alternative such as Google DNS (8.8.8.8). At this point, the resolver goes through a process called recursion to convert the domain name into an IP address.

The resolver starts by querying one of the root DNS servers for the IP of "www.google.com". This query does not have the recursive flag and therefore is an "iterative query", meaning its response must be an address, the location of an authoritative name server, or an error.

These root servers hold the locations of all of the top level domains (TLDs) such as .com, .net, .io

The root does not have the IP address of "www.google.com", but it knows that .com might know, so it returns the location of the .com servers. The root responds with a list of the 13 locations of the .com gTLD servers, listed as NS or "name server" records.

Next the resolver queries one the of the .com name servers for the IP address of "google.com".

Each TLD server holds a list of all of the authoritative name servers for each domain in the TLD.

The .com TLD server does not have the IP address for "google.com", but it knows the location of google.com's name servers. The .com TLD server responds with a list of all google.com's NS records. In this case google has 4 name servers, "ns1.google.com" to "ns4.google.com".

Finally, the DNS resolver queries one of Google's name server for the IP of "www.google.com".

This time the queried Name server know the IPs and responds with an A or AAAA address record.

At this point the resolver has finished the recursion process and is able to respond to the end user's operating system with an IP address.

At this point the operating system, now in possession of www.google.com's IP address, provides the IP to the browser, which initiate the TCP connection to start loading the page.

## What is TCP/IP?

TCP/IP refers to a suite of communication protocols used to connect network devices on the internet.

TCP/IP stands for Transmission Control Protocol/Internet Protocol.

The TCP/IP model is a four-layer reference model. Each layer corresponds to a set of protocols with a well-defined purpose:

1. Application layer
2. Transport layer
3. Internet or Network layer
4. Network Access or Link layer

The Application layer is the highest abstraction layer of the TCP/IP model that provides the interfaces and protocols needed by the users. It combines the functionalities of the session layers, the presentation layer and the application layer of the OSI logical model.

The Application Layer is resposible for providing various network services directly yo your applications. When you open a web page or start a file download, it's the Application Layer protocols like (HTTP, FTP) that your software (browser) interfaces with.

The Transport Layer is an end-to-end layer used to deliver messages to a host. It is termed an end-to-end layer because it provides a point-to-point connection rather than hop-to-hop, between the source host and destination host to deliver the services reliably.

At the sender's side: the transport layer recives data (message) from the application layer, divides it to segments, adds the source and destinations port numbers into the headerof the segment and transfers the message to the network layer.

At the receiver's side: the transport layer receives data from Network layer, reassembles the segmented data, reads its header, identifies the port number, and forwards the message to the appropriate port in the Application layer.

The Internet Layer of the TCP/IP model aligns with the Layer 3 (Network) layer of the OSI model.

The Internet Layer is responsible for routing packets of data from one device to another across a network. It does this by assigning each device a unique IP address, which is used to identify the device and determine the route that packets should take to reach it.

The TCP/IP connection is established in a three-way handshake:
1. **SYN(Synchronize):** Your computer, which is the client machine, sends a packet containing a sequence number to the server. This step indicates the intention of the client machine to establish a connection.
2. **SYN-ACK(Synchronize-Acknowledge):** Upon receiving the SYN packet, the server checks whether it has open ports to accept and initiate new connections. If there are open ports, it responds with a SYN-ACK packet. This packet has two crucial parts. First, it acknowledges receipt of the SYN packet by confirming the sequence number. Second, the server includes its sequence number to signify its readiness to establish a connection.
3. **ACK(Acknowledgement):** Upon receiving the SYN-ACK packet, the client machine responds with an ACK packet. This packet acknowledges receipt of the SYN-ACK packet and confirms the server’s sequence number.

After the three-way handshake, a connection is established, and the devices can reliably exchange data.

At this point, the browser sends a GET request asking for a google.com web page over the established TCP connection. The server receives the request and responds with the HTML code for the homepage of google.com. The browser will display the HTML skeleton, and if the web page requires additional resources, the browser sends out more requests. These additional requests can be for elements such as images, Javascript files, and CSS stylesheets.

## What is a Firewall?

Firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network.

The Firewall resides between the Internet and the Google Servers will examine the incoming and outgoing traffic between your computer and the server and based on its predeterminded security rules will allow or disallow the communication.

## What is HTTPS/SSL?

Hypertext Transfer Protocol (HTTP) is an application layer protocol (in the TCP/IP stack) for transmiting hypermedia documnets, such as HTML.

HTTP functions as a request–response protocol in the client–server model. A web browser, for example, may be the client whereas a process, named web server, running on a computer hosting one or more websites may be the server.

The client submits an HTTP request message to the server. The server, which provides resources such as HTML files and other content or performs other functions on behalf of the client, returns a response message to the client. The response contains completion status information about the request and may also contain requested content in its message body.

HTTP transmits unencrypted data, which means that information sent from a client can be intercepted and read by third parties. This was not an ideal process, so it was extended into HTTPS to add another layer of security to communication. HTTPS combines HTTP requests and responses with SSL and TLS technology.

SSL stand for Secure Socket Layer and TLS stands for Transport Layer Security

## How HTTPS Work?

1. The HTTP client sends an HTTP request to the HTTP server.
2. The HTTP server responds with a digital certificate as an SSL certificate containing a public key.
3. The HTTP client verifies that the certificate is valid:
    1. The HTTP client verifies that the certificate has not expired, the domain name in the certificate matches the one in the Request and the certificate is issued by a trusted CA.
    2. The HTTP client has a list of trusted CAs that it use to verifiy the certificate. If the CA that issued the certificate is on that list, the certificate will be trusted.
4. The HTTP client uses the certificate public key to encrypt and send back its own symmetric key.
5. The HTTP server then decrypts this symmetric key using its private key.
6. The HTTP server and client then use the symmetric key to encrypt and decrypt all messages between them, ensuring that no one else can intercept and read them.

## Load-Balancer

A load balancer is a device or software that distributes network traffic across multiple servers. It ensures that no single server becomes overwhelmed with requests, which can cause delays and downtime. Load balancers are important as they improve the performance and availability of applications by evenly distributing traffic across multiple servers. This can help to prevent bottlenecks and improve the overall user experience.

A load balancer acts as a traffic cop as it sits in front of the HTTP server farm and routes incoming requests to the appropriate HTTP server.

When a client (such as a user’s web browser) sends a request to the application, the request is first received by the load balancer. The load balancer then uses a load-balancing algorithm to determine which of the web servers should receive the request. The algorithm considers factors such as the current workload of each server, the server’s capacity, and the type of request sent.

Once the load balancer decides on the target server using a routing algorithm, it then forwards the request. The web server processes the request and sends back the response to the load balancer. Further, the load balancer forwards the response to the client.

## Web Server

A web server is a software component that delivers static data like images, files, and text in response to client requests.

A web server is technology that hosts a website’s code and data. When you enter a URL in your browser, the URL is actually the address identifier of the web server.

1. The browser uses the URL to find the server’s IP address
2. The browser sends an HTTP request for information
3. The web server communicates with a database server to find the relevant data
4. The web server returns static content such as HTML pages, images, videos, or files in an HTTP response to the browser
5. The browser then displays the information to you

## Application Server

An application server adds business logic to compute the web server's response. Both terms are used synonymously, and the most popular server software solutions today are hybrid web application servers.

An application server extends the capabilities of a web server by supporting dynamic content generation, application logic, and integration with various resources. It provides a runtime environment where you can run application code and interact with other software components, like messaging systems and databases. It uses business logic to transform data more meaningfully than a web server.

When you attempt to access interactive content on a website, the process works as follows:
1. The browser uses the URL to finds the server’s IP address
2. The browser sends an HTTP request for information
3. The web server transfers the request to the application server
4. The application server applies business logic and communicates with other servers and third-party systems to fulfill the request
5. The application server renders a new HTML page and returns it as a response to the web server
6. The web server returns the response to the browser
7. The browser displays the information to you

## How do application servers and web servers work together?

Application servers and web servers work together to handle client requests and deliver the correct content to the user. The web server always receives a new request first. If it can produce the information itself, it does so and sends back an HTTP response. It also checks that the data the user requested isn’t already in its cache.

If the web server can’t access the content the user requires, it forwards the request to the application server. The application server processes data and uses business logic to provide the correct information. It then passes the request back to the web server, which passes it on to the user. In certain architectures, you can also configure application servers to handle HTTP requests by themselves.







