function(doc) { 
     if (doc.doc_type == "Contact") 
          emit(doc._id, doc); 
}