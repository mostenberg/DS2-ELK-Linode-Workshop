from test import *
import json


# def sendDataToElastic(url,username,password,count,jsonData):

url = "http://170-187-149-159.ip.linodeusercontent.com:5601/datastream2/_bulk"
username = "ds2user"
password = "u34aB6RsO4I4%Uc2qYNGnVS4vlKpvA"
count = 1000

jsonData = """
{
  "version": 1,
  "streamId": "12345",
  "cp": "123456",
  "reqId": "1239f220",
  "reqTimeSec": "1678859500.171",
  "bytes": "4995",
  "cliIP": "128.147.28.68",
  "statusCode": "206",
  "proto": "HTTPS",
  "reqHost": "test.hostname.net",
  "reqMethod": "GET",
  "reqPath": "/path1/path2/file.ext",
  "reqPort": "443",
  "rspContentLen": "5000",
  "rspContentType": "text/html",
  "UA": "Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_14_3%29",
  "tlsOverheadTimeMSec": "0",
  "tlsVersion": "TLSv1",
  "objSize": "484",
  "uncompressedSize": "484",
  "overheadBytes": "232",
  "totalBytes": "0",
  "queryStr": "param=value",
  "accLang": "en-US",
  "cookie": "cookie-content",
  "range": "37334-42356",
  "referer": "https%3A%2F%2Ftest.referrer.net%2Fen-US%2Fdocs%2FWeb%2Ftest",
  "xForwardedFor": "8.47.28.38",
  "maxAgeSec": "3600",
  "reqEndTimeMSec": "3",
  "errorCode": "ERR_ACCESS_DENIED|fwd_acl",
  "turnAroundTimeMSec": "11",
  "transferTimeMSec": "125",
  "dnsLookupTimeMSec": "50",
  "lastByte": "1",
  "cacheStatus": "1",
  "cacheable": "1",
  "edgeIP": "23.50.51.173",
  "country": "US",
  "state": "Virginia",
  "city": "HERNDON",
  "serverCountry": "SG",
  "billingRegion": "8",
  "securityRules": "ULnR_28976|3900000:3900001:3900005:3900006:BOT-ANOMALY-HEADER|",
  "ewUsageInfo": "//4380/4.0/1/-/0/4/#1,2\\//4380/4.0/4/-/0/4/#0,0\\//4380/4.0/5/-/1/1/#0,0",
  "ewExecutionInfo": "c:4380:7:161:162:161:n:::12473:200|C:4380:3:0:4:0:n:::6967:200|R:4380:20:99:99:1:n:::35982:200",
  "customField": "any-custom-value"
}

"""
print("JSon data is: "+jsonData)
sendDataToElastic(url, username, password, count, jsonData)
