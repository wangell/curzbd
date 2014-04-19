#!/usr/bin/python

import urllib.request
import urllib.error
import json

class SabnzbdApi:
    def __init__(self, config_dic):
        self.config = dict()
        self.config['host'] = config_dic['Host']
        self.config['port'] = config_dic['Port']
        self.config['apikey'] = config_dic['ApiKey']
        self.config['http_method'] = config_dic['HttpMethod']

    def sab_request(self, sub_url):
        resp = ""
        url_g = self.config['http_method'] + "://" + self.config['host'] + ":" + self.config['port'] + "/sabnzbd/api?" + sub_url + "&apikey=" + self.config['apikey']
        with urllib.request.urlopen(url_g) as cur_req:
            resp = cur_req.read().decode('utf-8')
        return resp

    def queue_output(self, q_strings):
        j = json.loads(self.sab_request("mode=queue&output=json"))
        return j

    def history_output(self, q_strings):
        j = json.loads(self.sab_request("mode=history&output=json"))
        return j

    def get_version(self, q_strings):
        j = json.loads(sab_request("mode=version&output=json"))
        return j["version"]

    def get_authtype(self, q_strings):
        j = sab_request("mode=auth")
        return j.rstrip()

    def del_queue_item(self, nzo_ids):
        j = self.sab_request("mode=queue&name=delete&value=" + (',').join(nzo_ids))

    def add_nzb_url(self, q_strings):
        j = sab_request("mode=addurl&name=" + q_strings[0] + "&nzbname=" + q_strings[1])

    def set_dl_speed(self, q_strings):
        j = sab_request("mode=config&name=speedlimit&value=" + q_strings[0])
