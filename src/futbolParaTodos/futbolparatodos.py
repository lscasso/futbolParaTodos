# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
import urllib2
import xbmc
import xbmcplugin
import xbmcgui
import CommonFunctions
common = CommonFunctions
common.plugin = "futbolParaTodos"

url = "http://www.futbolparatodos.com.ar"
youtube = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="
addon_handle = int(sys.argv[1])

def parseVideo(urlP):
    req = urllib2.Request(url + urlP)
    print url + urlP
    req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    page=response.read()
    lis = common.parseDOM(page,"iframe")
    print lis.get("src").split("/")[4]
    return lis.get("src").split("/")[4]

print "0lala"
req = urllib2.Request(url)
print "1"
req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
response = urllib2.urlopen(req)
print "2"
page=response.read()
print "3"
response.close
print "3.1"
ret = common.parseDOM(page, "div",attrs = { "id": "div-partidodetalle-" } )
print "4"
progress = xbmcgui.DialogProgress()
progress.create('Progress', 'This is a progress bar.')
i = 1
for partidos in ret:
    percent = i * 100 / len(ret) 
    i = i + 1
    progress.update( percent, "", "Opa ganfa", "" )
    envivo = common.parseDOM(partidos,"div", {"class" : "botonenvivo"})
    if len(envivo) > 0:
        equipos = common.parseDOM(partidos, 'span',{"class" :"nombreclub"})
        print equipos[0] + " " + equipos[1]
        li = xbmcgui.ListItem(equipos[0].text + ' - '  + equipos[1].text, iconImage='DefaultVideo.png')
        li.setProperty("IsPlayable", "true")
        info = {
            'Title': 'Lala'
        }
        li.setInfo( type="Video", infoLabels=info )
        videoID = parseVideo(link.get("href"))
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=youtube.format(id=videoID) , listitem=li, isFolder=False)
xbmcplugin.endOfDirectory(addon_handle)