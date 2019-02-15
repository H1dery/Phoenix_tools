#coding=utf-8
## __author__ = "Fidcer" ##
import nmap
import threading
import write_html


lock = threading.Lock()
threads = []
Scan_Ports_Version = []
def nmapScan(Host,Port):
    # 调用nmap的PortScanner类
    nm = nmap.PortScanner() 
    # 使用scan方法进行扫描
    results = nm.scan(Host, str(Port),'-sV -Pn --host-timeout 100s')
    state = results['scan'][Host]['tcp'][Port]['state']
    ser_info = results['scan'][Host]['tcp'][int(Port)]['extrainfo']
    ser_version = results['scan'][Host]['tcp'][int(Port)]['product'] + results['scan'][Host]['tcp'][int(Port)]['version']
    if state == 'open':
        #lock.acquire()
        #print("[+] {} tcp/{} {} version:{} ({})".format(Host, Port, state,ser_version,ser_info))
        scan_results = "[+] {} tcp/{} {} version:{} ({})".format(Host, Port, state,ser_version,ser_info)
       # print(scan_results)
        Scan_Ports_Version.append(scan_results)

        #write_html.template_scan_results(Host,scan_results)
        #lock.release()
    else:
    	pass


def thread_scan(Host,Port):

    t = threading.Thread(target=nmapScan,args=(Host,Port))
    threads.append(t)
    t.start()

    for t in threads:
        t.join()


