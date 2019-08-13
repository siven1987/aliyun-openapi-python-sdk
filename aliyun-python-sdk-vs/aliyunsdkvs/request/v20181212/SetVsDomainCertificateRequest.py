# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvs.endpoint import endpoint_data

class SetVsDomainCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'SetVsDomainCertificate','vs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SSLProtocol(self):
		return self.get_query_params().get('SSLProtocol')

	def set_SSLProtocol(self,SSLProtocol):
		self.add_query_param('SSLProtocol',SSLProtocol)

	def get_CertType(self):
		return self.get_query_params().get('CertType')

	def set_CertType(self,CertType):
		self.add_query_param('CertType',CertType)

	def get_ShowLog(self):
		return self.get_query_params().get('ShowLog')

	def set_ShowLog(self,ShowLog):
		self.add_query_param('ShowLog',ShowLog)

	def get_SSLPri(self):
		return self.get_query_params().get('SSLPri')

	def set_SSLPri(self,SSLPri):
		self.add_query_param('SSLPri',SSLPri)

	def get_ForceSet(self):
		return self.get_query_params().get('ForceSet')

	def set_ForceSet(self,ForceSet):
		self.add_query_param('ForceSet',ForceSet)

	def get_CertName(self):
		return self.get_query_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_query_param('CertName',CertName)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SSLPub(self):
		return self.get_query_params().get('SSLPub')

	def set_SSLPub(self,SSLPub):
		self.add_query_param('SSLPub',SSLPub)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)