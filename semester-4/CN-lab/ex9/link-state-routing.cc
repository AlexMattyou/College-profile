// Link State Routing Simulation
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/netanim-module.h"
#include "ns3/ospf-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("LinkStateRouting");

int main (int argc, char *argv[])
{
    CommandLine cmd;
    cmd.Parse (argc, argv);

    // Create nodes
    NodeContainer nodes;
    nodes.Create (4);

    // Create point-to-point links
    PointToPointHelper pointToPoint;
    pointToPoint.SetDeviceAttribute ("DataRate", StringValue ("5Mbps"));
    pointToPoint.SetChannelAttribute ("Delay", StringValue ("2ms"));

    NetDeviceContainer devices;
    devices = pointToPoint.Install (nodes.Get (0), nodes.Get (1));
    devices = pointToPoint.Install (nodes.Get (1), nodes.Get (2));

    // Install the internet stack on the nodes
    InternetStackHelper stack;
    stack.Install (nodes);

    // Assign IP addresses
    Ipv4AddressHelper address;
    address.SetBase ("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces = address.Assign (devices);

    // Install and configure OSPF routing protocol
    OspfHelper ospf;
    ospf.Install (nodes.Get (0), interfaces.GetAddress (0), nodes.Get (1), interfaces.GetAddress (1), 1);
    ospf.Install (nodes.Get (1), interfaces.GetAddress (1), nodes.Get (2), interfaces.GetAddress (2), 1);

    // Add OSPF interfaces to the global routing table
    Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

    // Run simulation
    Simulator::Run ();
    Simulator::Destroy ();

    return 0;
}
