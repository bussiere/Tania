function(doc) { 
     if (doc.doc_type == "Pret") 
          emit(doc._id, doc); 
}