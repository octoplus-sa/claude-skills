# Sockets Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 494-496).

## Index (line numbers in this file)

- `<< Accept` — L43
- `<< Close` — L77
- `<< Connect` — L85
- `<< Get Sock Name` — L109
- `<< GetPeerName` — L98
- `<< Listen` — L129
- `<< Show Schedule` — L20
- `<< Stop` — L22
- `Pie Seg()` — L26
---

Segment Message

sch<<Show Schedule()
Shows a list of all scheduled events.
sch<<Stop()
Stops the scheduler from running all scheduled events.

Segment Message
Pie Seg(<style>, {x, y}, radius, [values])
Description

Creates a pie seg at the specified origin, with the specified radius, based on given values.
Required Arguments
{x, y} Specifies the x and y coordinates at which the pie seg is displayed.

radius Specifies the radius.
values Specifies the values specified in matrix format.
Optional Argument

style A quoted string that specifies the style: "Pie" (traditional pie chart with each slice
sized by the Summary Statistic), "Ring" (each variable or level of a stratifying variable
is represented by a concentric ring), or "Coxcomb" (the central angles for all slices are
equal).

Sockets Messages
skt<<Accept(<callback, timeout>)
Description

Tells the server socket to accept a connection and return a new connected socket.
Returns

A list of up to four items. The first is a quoted string that echoes the command
("accept"). The second is a quoted string, either "ok" or an error. The third is a quoted
string that specifies the name of the machine that just connected. The fourth is a reference
to the socket that you can send more messages.
Optional Arguments

callback Specifies the name of a function to receive the data.

JSL Messages
Sockets Messages

495

timeout If you use a callback, timeout specifies how long the function should wait for
an answer. For a server socket, 0 is an acceptable value because a server should not shut
down because no one has connected to it recently.
skt<<bind(localhost, port)
Description

Associates a port on the local machine with the socket.
Returns

A list of two quoted strings. The first string is the command name (“bind”) and the second
is “ok” if successful or an error.
Required Arguments

localhost Specifies the quoted local machine. You cannot bind to another machine.
port Specifies the port that should be used.
skt<<Close()
Description

Closes a socket.
Returns

A list of two quoted strings. The first string is the command name (“close”) and the second
is “ok” if successful.
skt<<Connect(socketname, port)
Description

Connects to a listening socket.
Returns

A list of two quoted strings. The first string is the command name (“connect”) and the
second is “ok” for a successful connection or an error sent back by the other socket.
Arguments

socketname Specifies the name of the other socket. If you are connecting to a web server,
this is the web address (the name is preferred to the IP address).
port Specifies the port of the other socket to connect through.
skt<<GetPeerName()
Description

Retrieves the address and port of the socket at the other end of the connection.

Sockets Messages

Returns

A list of four quoted strings. The first echoes the command ("getpeername"). The second
is either “ok” or an error. The third and fourth are the address and the port.
skt<<Get Sock Name()
Description

Retrieves the address and port of the socket at this end of the connection.
Returns

A list of four quoted strings. The first echoes the command ("getsockname"). The second
is either “ok” or an error. The third and fourth are the address and the port.
skt<<ioctl(FIONBIO, Boolean)
Description

Controls the socket’s blocking behavior.
Returns

A list of two quoted strings. The first string is the command name (“ioctl”) and the second
is “ok” if successful or an error.
Arguments
FIONBIO, 1 FIONBIO means Non-Blocking I/O. If true, turns on the behavior and the

argument.
skt<<Listen()
Description

Tells the server socket to listen for connections.
Returns

A list of two quoted strings. The first echoes the command ("listen") and the second is
"ok" or an error message.
skt<<recv(n, <callback, timeout>)
skt<<recvfrom(n, <callback, timeout>)
Description

Receives either a stream message (recv) or a datagram message (recvfrom) from the other
socket. If the two optional arguments are used, the data is not received immediately.
Instead, the data is received when the function callback is called.
Returns

A list of three quoted strings. The first string is the command name (“recv” or “recvto”).
The second is “ok” if successful or an error message if not. The third string is the data that
