""" 
owtf is an OWASP+PTES-focused try to unite great tools and facilitate pen testing
Copyright (c) 2011, Abraham Aranguren <name.surname@gmail.com> Twitter: @7a_ http://7-a.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;

ACTIVE Plugin for Testing for HTTP Methods and XST (OWASP-CM-008)
"""

DESCRIPTION = "Active probing for HTTP methods"

def run(Core, PluginInfo):
	#Core.Config.Show()
	#Transaction = Core.Requester.TRACE(Core.Config.Get('HOST_NAME'), '/')
	URL = Core.Config.Get('TOP_URL')
	# TODO: PUT not working right yet
	#PUT_URL = URL+"/_"+Core.Random.GetStr(20)+".txt"
	#print PUT_URL
	#PUT_URL = URL+"/a.txt"
	PUT_URL = URL
	Content = Core.Reporter.DrawHTTPTransactionTable( [ Core.Requester.GetTransaction(True, URL, 'TRACE'), Core.Requester.GetTransaction(True, URL, 'DEBUG'), Core.Requester.GetTransaction(True, PUT_URL, 'PUT', Core.Random.GetStr(15)) ] ) 
	Content += Core.PluginHelper.DrawCommandDump('Test Command', 'Output', Core.Config.GetResources('ActiveHTTPMethods'), PluginInfo, Content)
	# Deprecated: Content += Core.PluginHelper.LogURLs(PluginInfo, Core.Config.GetResources('ActiveHTTPMethodsExtractLinks'))
	return Content

