function(doc) { 
     if (doc.doc_type == "Lien") 
          emit(doc._id, doc); 
}