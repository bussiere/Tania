function(doc) { 
     if (doc.doc_type == "Presentation") 
          emit(doc._id, doc); 
}