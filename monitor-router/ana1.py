from scapy.all import *


def main():
    data = "capture.eth0"
    a = rdpcap(data)
    sessions = a.sessions()
    print(sessions)

if __name__ == "__main__":
    main()