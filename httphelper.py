import urllib2
import json
from urllib2 import HTTPError
from httplib import BadStatusLine

def call_service(url, method='GET', body=None, contentType='application/json', accept='application/json', debug=False):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, data=body)
    request.get_method = lambda: method

    request.add_header('Content-Type', contentType)
    request.add_header('Accept', accept)
    ok = False
    try:
        resp  = opener.open(request)
        data = resp.read()
        ok = True
    except HTTPError as exc:
        resp = exc
        data = exc.read()
    except IOError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

    if resp and debug:
        print "Service response: %s (%d)" % (resp.msg, resp.getcode())

    return ok, data

def print_json(json_text):
    print json.dumps(json.loads(json_text),sort_keys=False, indent=2)