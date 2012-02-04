function(doc) { 
     if (doc.doc_type == "Note") 
          emit(doc._id, doc); 
}