function(doc) { 
     if (doc.doc_type == "Item") 
          emit(doc._id, doc); 
}