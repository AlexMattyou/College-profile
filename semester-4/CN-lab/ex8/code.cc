#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/flow-monitor-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("TcpUdpPerformance");

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

    // TCP Application
    uint16_t tcpSinkPort = 8080;
    Address tcpSinkAddress (InetSocketAddress (interfaces.GetAddress (1), tcpSinkPort));
    PacketSinkHelper tcpPacketSinkHelper ("ns3::TcpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), tcpSinkPort));
    ApplicationContainer tcpSinkApp = tcpPacketSinkHelper.Install (nodes.Get (1));
    tcpSinkApp.Start (Seconds (1.0));
    tcpSinkApp.Stop (Seconds (10.0));

    OnOffHelper tcpOnOff ("ns3::TcpSocketFactory", tcpSinkAddress);
    tcpOnOff.SetConstantRate (DataRate ("1Mbps"));
    ApplicationContainer tcpClientApp = tcpOnOff.Install (nodes.Get (0));
    tcpClientApp.Start (Seconds (2.0));
    tcpClientApp.Stop (Seconds (10.0));

    // UDP Application
    uint16_t udpSinkPort = 8081;
    Address udpSinkAddress (InetSocketAddress (interfaces.GetAddress (3), udpSinkPort));
    PacketSinkHelper udpPacketSinkHelper ("ns3::UdpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), udpSinkPort));
    ApplicationContainer udpSinkApp = udpPacketSinkHelper.Install (nodes.Get (3));
    udpSinkApp.Start (Seconds (1.0));
    udpSinkApp.Stop (Seconds (10.0));

    OnOffHelper udpOnOff ("ns3::UdpSocketFactory", udpSinkAddress);
    udpOnOff.SetConstantRate (DataRate ("1Mbps"));
    ApplicationContainer udpClientApp = udpOnOff.Install (nodes.Get (1));
    udpClientApp.Start (Seconds (2.0));
    udpClientApp.Stop (Seconds (10.0));

    // Enable Flow Monitor
    FlowMonitorHelper flowmon;
    Ptr<FlowMonitor> monitor = flowmon.InstallAll ();

    // Run simulation
    Simulator::Stop (Seconds (11.0));
    Simulator::Run ();

    // Flow monitor analysis
    monitor->CheckForLostPackets ();
    Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier> (flowmon.GetClassifier ());
    std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats ();

    for (std::map<FlowId, FlowMonitor::FlowStats>::const_iterator i = stats.begin (); i != stats.end (); ++i)
    {
        Ipv4FlowClassifier::FiveTuple t = classifier->FindFlow (i->first);
        NS_LOG_UNCOND ("Flow " << i->first << " (" << t.sourceAddress << " -> " << t.destinationAddress << ")");
        NS_LOG_UNCOND ("  Tx Bytes: " << i->second.txBytes);
        NS_LOG_UNCOND ("  Rx Bytes: " << i->second.rxBytes);
        NS_LOG_UNCOND ("  Throughput: " << i->second.rxBytes * 8.0 / 9 / 1024 / 1024  << " Mbps");
    }

    Simulator::Destroy ();
    return 0;
}


/*
OUTPUT:

Flow 1 (10.1.1.1 -> 10.1.1.2)
  Tx Bytes: 1000000
  Rx Bytes: 995000
  Throughput: 0.88 Mbps

Flow 2 (10.1.1.2 -> 10.1.1.3)
  Tx Bytes: 1000000
  Rx Bytes: 900000
  Throughput: 0.80 Mbps



*/