import urllib.request as urllib
import re

def main():
	baseUrls = ["http://flynn.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=190341&sessionid=b258326d94bfc9209c57c1309b184657", "http://artzerounian.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=140663&sessionid=b258326d94bfc9209c57c1309b184657","http://george.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=140739&sessionid=b258326d94bfc9209c57c1309b184657", "http://jones.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=168036&sessionid=b258326d94bfc9209c57c1309b184657", "http://rebecca.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=140537&sessionid=b258326d94bfc9209c57c1309b184657", "http://landis.seniorhigh.spring-ford.net/modules/tt/profile.phtml?profile_id=137427&sessionid=b258326d94bfc9209c57c1309b184657"]
	for baseUrl in baseUrls:
		crawl(baseUrl, 0, 1)


def crawl(url, depth, maxDepth):
	try:
		# get page source
		handle = urllib.urlopen(url)
		pageSource = str(handle.read())
		# get new links
		newUrls = re.findall(r"\<a[^h]+href=[\'\"](http:\/\/[^\'\"]+)",	pageSource)
		
		# make recursive calls to new links
		if(depth < maxDepth):
			for newUrl in newUrls:
				if "seniorhigh.spring-ford.net" in newUrl and "translate" not in newUrl:
					crawl(newUrl, depth + 1, maxDepth)
	except:
		# print dead link
		print(url + "\n")
			
main()