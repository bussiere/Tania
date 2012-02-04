function(doc) { 
     if (doc.doc_type == "Tips") 
          emit(doc._id, doc); 
}