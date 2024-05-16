// Distance Vector Routing Simulation
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/csma-module.h"
#include "ns3/dsdv-helper.h"
#include "ns3/internet-stack-helper.h"
#include "ns3/ipv4-address-helper.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("DistanceVectorRouting");

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

    // Create a CSMA network
    CsmaHelper csma;
    csma.SetChannelAttribute ("DataRate", StringValue ("100Mbps"));
    csma.SetChannelAttribute ("Delay", TimeValue (NanoSeconds (6560)));

    NetDeviceContainer csmaDevices;
    csmaDevices = csma.Install (nodes.Get (1), nodes.Get (3));

    // Install the internet stack on the nodes
    InternetStackHelper stack;
    stack.Install (nodes);

    // Assign IP addresses
    Ipv4AddressHelper address;
    address.SetBase ("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces = address.Assign (devices);
    address.SetBase ("10.1.2.0", "255.255.255.0");
    interfaces = address.Assign (csmaDevices);

    // Install and configure DSDV routing protocol
    DsdvHelper dsdv;
    dsdv.Install (nodes);

    // Set up routing tables
    Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

    // Run simulation
    Simulator::Run ();
    Simulator::Destroy ();

    return 0;
}
