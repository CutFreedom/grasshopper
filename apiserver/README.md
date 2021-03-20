# Goal

The goal of this effort is to replace `api.cricut.com` with a local
server, entirely detached from the upstream server. This can provide
functionality when a user is not connected to the internet, or simply
when a user chooses to keep all data local/private.

There are three main points to using this server:

* modify `/etc/hosts` to point `api.cricut.com` to localhost
  (or the Windows equivalent? help?), and run the server locally
* modify the DNS server used by the client/desktop to point
  to an instance of this server
* configuring/running this server to manage requests
