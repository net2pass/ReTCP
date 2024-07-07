import pydivert
def sniff_and_modify():
    #record sent last packet is SYN
    record={}
    with pydivert.WinDivert("tcp.DstPort == 443") as w:
        print("Sniffing TCP packets...")
        for packet in w:
            # default : send all packet.
            w.send(packet)  
            if packet.is_outbound:
                if packet.tcp and packet.tcp.syn:
                    record[packet.src_port] = True
                if packet.tcp and packet.tcp.ack and packet.tcp.psh==False:
                    # At Here Inject corrupt packet.
                    if packet.src_port in record and record[packet.src_port] == True:
                        #print(packet)
                        packet.tcp.payload=b'RAHAHAHAHAHAAAAAAA'
                        packet.tcp.cksum=65521
                        packet.tcp.ack_num=packet.tcp.ack_num+650022
                        w.send(packet,False)
                        print("[TCP Jailbreak]:",packet.dst_addr)
                    # Okay.
                  
sniff_and_modify()
