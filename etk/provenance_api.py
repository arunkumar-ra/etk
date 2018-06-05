from etk.origin_record import OriginRecord
from functools import reduce
import itertools
class ProvenanceAPI:

	def __init__(self, doc):
		self.origin_doc = doc

	def get_origins(self, field:str=None, index:int = None, value:str=None):
		origins = []
		if value == None:
			if index == None:
				items = self.origin_doc.kg.value[field]
				for item in items:
					search_string = item["value"]
					kg_provenance_ids = self.origin_doc.kg_provenances[search_string]#.get_origins(search_string)
				
					for kg_provenance_id in kg_provenance_ids:
						kg_provenance = self.origin_doc.provenances[kg_provenance_id]
						origins.extend(kg_provenance.get_origins(search_string))
			else:
				search_string = self.origin_doc.kg.value[field][index]["value"]
				kg_provenance_ids = self.origin_doc.kg_provenances[search_string]#.get_origins(search_string)
				for kg_provenance_id in kg_provenance_ids:
					kg_provenance = self.origin_doc.provenances[kg_provenance_id]
					origins.extend(kg_provenance.get_origins(search_string))
				
		else:
			kg_provenance_ids = self.origin_doc.kg_provenances[value]#.get_origins(search_string)
			for kg_provenance_id in kg_provenance_ids:
				kg_provenance = self.origin_doc.provenances[kg_provenance_id]
				origins.extend(kg_provenance.get_origins(value))
		return origins

	def get_methods(self, field:str=None, index:int = None, value:str=None):
		search_string = self.origin_doc.kg.value[field][index]["value"]
		methods = kg_provenance.get_methods(search_string)
		return methods
		#print ("searchString"+ str(search_string))
		'''provenances = self.origin_doc.cdr_document["provenances"]
		origins:List[OriginRecord] = []
		for provenance in provenances:
		    if provenance["@type"] == 'kg_provenance_record' and provenance["value"] == search_string:
		        origins.append(get_methods(provenance))
		return origins'''
