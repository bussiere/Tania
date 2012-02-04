function(doc) { 
     if (doc.doc_type == "Page") 
          emit(doc._id, doc); 
}