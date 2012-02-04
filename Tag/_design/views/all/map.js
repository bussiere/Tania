function(doc) { 
     if (doc.doc_type == "Tag") 
          emit(doc._id, doc); 
}