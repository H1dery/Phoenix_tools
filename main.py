#coding=utf-8
## __author__ = "Fidcer" ##
import Phoenix_scan
import argparse
import re,sys
import socket
import write_html
import Web_Directory

def main():
    PortList = [21, 22, 23, 25, 80, 135, 137, 139, 443, 445, 1433, 1502, 3306, 3389, 8080, 9015]
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='Host', help="Host like: 192.168.3.1 or http://localhost")
    parser.add_argument('-p', dest='Ports', nargs='+', type=int, help="Port like: 80 443 21,Default Scan Ports 21, 22, 23, 25, 80, 135, 137, 139, 445, 443, 1433, 1502, 3306, 3389, 8080, 9015",default=PortList)
    parser.add_argument('-T', dest='Threads',type=int,help="Thread number,Default:2",default=2)
    args = parser.parse_args()
    if args.Host == None or args.Ports == None:
        parser.print_help()
        sys.exit(0)
    try:
        Host_split = args.Host.split('://')[1]
    except:
        parser.print_help()
        sys.exit(0)
    Host = Host_split
    Ports = args.Ports
    ip_search = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if ip_search.match(Host):#匹配是否为ip
        for Port in Ports:
            Phoenix_scan.nmapScan(Host,Port)
    else:
        try:
            domain_ip = socket.gethostbyname(Host)
        except:
            print("please Enter the correct domain name.")
            sys.exit(0)
        for Port in Ports:
            Phoenix_scan.nmapScan(domain_ip,Port)
        #Ports_Version_List = Phenix_scan.Scan_Ports_Version
        #print(Ports_Version_List)
       # print(Phoenix_scan.Scan_Ports_Version)
        Scan_Ports_Joins = ('\r\n<br>'.join(str(d) for d in Phoenix_scan.Scan_Ports_Version))
        ScanPort_write = str(Scan_Ports_Joins)
        write_html.template_scan_results(Host,ScanPort_write)
        Web_Directory.scan_web_dirb(args.Host+'/',args.Threads)
        #print()
        Scan_Dirbs_Joins = ('\r\n<br>'.join(str(d) for d in Web_Directory.webdirb_list))
        ScanDirbs = str(Scan_Dirbs_Joins)
        write_html.template_web_dirb(Host,ScanDirbs)
if __name__ == '__main__':
	main()