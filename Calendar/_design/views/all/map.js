function(doc) { 
     if (doc.doc_type == "Calendar") 
          emit(doc._id, doc); 
}