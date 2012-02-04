function(doc) { 
     if (doc.doc_type == "Droit") 
          emit(doc._id, doc); 
}