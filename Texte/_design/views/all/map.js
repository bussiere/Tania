function(doc) { 
     if (doc.doc_type == "Texte") 
          emit(doc._id, doc); 
}