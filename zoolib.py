# Author: pidpawel <pidpawel.eu>
# URL: https://pidpawel.eu/zoo/
# License: CC-BY-SA http://creativecommons.org/licenses/by-sa/3.0/pl/
import socket
import time
import threading
import sh
import json

special_hosts = (
	'deadbeef' 		# RW node
	)

def _get_revdns(host):
	try:
		(hostname, aliaslist, addrlist) = socket.gethostbyaddr(host)
		return hostname
	except socket.herror:
		return host

def discovery(hostnames=True,targets=[]):
	if not targets:
		targets = ["nodes"]

	discovery = sh.avahi_browse('-trp', '_ssh._tcp').split('\n')
	
	hosts = []
	for host in discovery:
		host = host.split(';')
		if host[0] == '=' and ( 'avahi' in targets \
				                or ( 'nodes' in targets and host[3][:5] == 'node-' ) \
				                or ( 'special' in targets and host[3] in special_hosts ) ):
			if hostnames:
				hosts.append(_get_revdns(host[7]))
			else:
				hosts.append(host[7])
	return hosts

def host_exec(host, cmd):
	return str(sh.ssh('root@'+host, '-o StrictHostKeyChecking=no', cmd)).rstrip('\n')

class execThread(threading.Thread):
	def __init__(self, host, cmd):
		threading.Thread.__init__(self)
		self.host = host
		self.cmd = cmd
	def run(self):
		self.r = host_exec(self.host, self.cmd)

def cluster_exec(targets, cmd):
	threads = []
	for host in targets:
		thread = execThread(host, cmd)
		thread.start()
		threads.append(thread)

	results = {}
	for thread in threads:
		thread.join()
		results[thread.host] = thread.r

	return results

def host_sysinfo(host):
	return json.loads(host_exec(host, 'zoo-sysinfo'))

def cluster_sysinfo(targets):
	r = cluster_exec(targets, 'zoo-sysinfo')
	for hostname, data in r.items():
		r[hostname] = json.loads(data)
	return r
