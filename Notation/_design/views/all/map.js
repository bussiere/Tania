function(doc) { 
     if (doc.doc_type == "Notation") 
          emit(doc._id, doc); 
}