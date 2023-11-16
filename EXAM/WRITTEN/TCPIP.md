# TCP/IP

## [Switching Technology](http://www.tcpipguide.com/free/t_CircuitSwitchingandPacketSwitchingNetworks.htm)

## [MPLS Fundamentals](https://www.geeksforgeeks.org/multi-protocol-label-switching-mpls/)

## [Signalling Protocols](https://en.wikipedia.org/wiki/Signaling_protocol) -- Don't know how useful this is

## [Carrier Ethernet](https://www.tutorialspoint.com/what-is-carrier-ethernet)

## [LDP](https://en.wikipedia.org/wiki/Label_Distribution_Protocol) -- Related to MPLS

### <https://www.ecb.torontomu.ca/~courses/ee8211/L8_TE.pdf>

## [IP Traffic Engineering](https://network-insight.net/2015/09/11/network-traffic-engineering/)

### <https://www.omscs-notes.com/computer-networks-old/traffic-engineering/>

## [ECMP](https://en.wikipedia.org/wiki/Equal-cost_multi-path_routing)

## [SBR](https://success.myshn.net/Skyhigh_Secure_Web_Gateway_(On_Prem)/Secure_Web_Gateway_Appliance_System/Source-based_Routing)

## [Routing Extensions for Traffic Engineering]

Q.17 . What are the routing extensions available
for traffic engineering ?
Ans . Routing extensions available for traffic engineering are as follows:
It is Extensions to the Intermediate System to Intermediate System ( IS- IS ) protocol to support Traffic Engineering ( TE). 
The IS - IS
protocol is specified in ISO 10589 , with extensions for supporting IPv4.
Each Intermediate System (IS) ( router) advertises one or more IS -IS
Link State Protocol Data Units ( LSPs) with routing information.
Each LSP is composed of a fixed header and a number of tuples,
each consisting of a Type , a Length and a Value .
Such tuples are commonly known as TLVs and are a good way of
encoding information in a flexible and extensible format.s
The Extended IS Reachability TLV :
The existing IS reachability ( TLV type 2 , defind in ISO 10589)
contains information about a series of IS neighbors.
For each neighbor, there is a structure that contains the default
metric, the delay, the monetary cost, the reliability and the 7- octet
ID of the adjacent neighbor.
Of this information , the default metric is commonly used . The
default metric is currently one octet , with one bit used to indicate
whether the metric is internal or external and one bit that was
originally unused , but which was later defined by [ RFC5302] to be
the up /down bit.
The remaining 6 bits are used to store the actual metric , resulting in
a possible metric range of 0-63 .
The remaining three metrics ( delay, monetary cost and reliability )
are not commonly implemented and reflect unused overhead in the
TLV.
The neighbor is identified by its system ID, typically 6 octets, plus
one octet indicating the pseudonode number . Thus , the existing TLV
consumes 11 octets per neighbor , with 4 octets for metric and 7
octets for neighbor identification. To indicate multiple adjacencies ,
this structure is repeated within the IS reachability TLV .
Because the TLV is limited to 255 octets of content , a single TLV
can describe up to 23 neighbors .
The IS reachability TLV can be repeated within the LSP fragments
to describe further neighbors . The proposed extended IS reachability
TLV contains a new data structure , consisting of:
7 octets system ID ad pseudonode number .
IS -IS Extensions for Traffic Engineering;( 1 )
It is Extensions to the Intermediate System to Intermediate System
3 octets of default metric.
1 octet of length of sub -TLVs 0-244 octets of sub -TLVs, where each ub-TLV consists of a sequence of 1 octet of sub-type 1 octet of
length of the Value field of the sub-TLV 0-242 octets of value .
Thus , if no sub- TLV are used, the new encoding requires 11 octets and can
contain up to 23 neighbors .
While the encoding allows for 255 octets of sub-TLVs , the maximum value
cannot fit in the overall IS reachability TLV .
Extensions to the OSPF protocol version 2 :
The extensions provide a way of describing the traffic engineering
topology (including bandwidth and administrative constraints) and
distributing this information within a given OSPF area.
This topology does not necessarily match the regular routed
topology , through this proposal depends on Network LSAs to
describe multi - access links.
Furthermore, no changes have been made to the operation of
OSPFv2 flooding, in particular, if non - TE capable nodes exist in the
topology, they MUST flood TE LSAs as any other type 10 ( area
local scope) Opaque LSAS .
The information made available by these extensions can be used to
build an extended link state database just as router LSAs are used to
build a "regular" link state database , the difference is that the
extended link state database ( referred to below as the traffic
engineering database ) has additional link attributes .
Uses of the traffic engineering database include:
Monitoring the extended link attributes
.
Local constraint - based source routing and
Global traffic engineering 

## [IS-IS](https://en.wikipedia.org/wiki/IS-IS) - Intermediate System to Intermediate System Protocol -- Part of routing extensions to traffic engineering

## [IPsec](https://www.geeksforgeeks.org/ip-security-ipsec/)

### <https://en.wikipedia.org/wiki/IPsec>

## [IPv6](https://en.wikipedia.org/wiki/IPv6)

## [IPv4 vs IPv6](https://www.ibm.com/docs/en/zos/2.3.0?topic=6-comparison-ipv6-ipv4-characteristics)

## [ACL](https://www.geeksforgeeks.org/access-lists-acl/)

## []()
