function(doc) { 
     if (doc.doc_type == "Utilisateur") 
          emit(doc._id, doc); 
}