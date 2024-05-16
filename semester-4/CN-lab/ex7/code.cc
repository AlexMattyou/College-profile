#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("CongestionControlSimulation");

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
    devices = pointToPoint.Install (nodes.Get (0), nodes.Get (2));
    devices = pointToPoint.Install (nodes.Get (1), nodes.Get (2));
    devices = pointToPoint.Install (nodes.Get (2), nodes.Get (3));

    // Install the internet stack on the nodes
    InternetStackHelper stack;
    stack.Install (nodes);

    // Assign IP addresses
    Ipv4AddressHelper address;
    address.SetBase ("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces = address.Assign (devices);

    // Create TCP applications
    uint16_t sinkPort = 8080;
    Address sinkAddress (InetSocketAddress (interfaces.GetAddress (1), sinkPort));
    PacketSinkHelper packetSinkHelper ("ns3::TcpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), sinkPort));
    ApplicationContainer sinkApp = packetSinkHelper.Install (nodes.Get (1));
    sinkApp.Start (Seconds (1.0));
    sinkApp.Stop (Seconds (10.0));

    OnOffHelper onoff ("ns3::TcpSocketFactory", sinkAddress);
    onoff.SetConstantRate (DataRate ("1Mbps"));
    ApplicationContainer clientApp = onoff.Install (nodes.Get (0));
    clientApp.Start (Seconds (2.0));
    clientApp.Stop (Seconds (10.0));

    // Enable tracing
    AsciiTraceHelper ascii;
    pointToPoint.EnableAsciiAll (ascii.CreateFileStream ("congestion-control-simulation.tr"));
    pointToPoint.EnablePcapAll ("congestion-control-simulation");

    // Run simulation
    Simulator::Run ();
    Simulator::Destroy ();

    return 0;
}


