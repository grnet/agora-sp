function search(list, termText) {
    if (termText === "") return list;
  
    let terms = termText.toLowerCase().split(",");
  
    if (terms.length === 0) return list;
    let results = list.filter(function (item) {
      for (let term of terms) {
        let termtokens = term.match(/\S+/g) || [];
        let cleanterm = termtokens.join(" ");
        if (cleanterm === "") continue;
  
        for (let subterm of item.terms) {
          if (subterm.includes(cleanterm)) {
            return item;
          }
        }
      }
      return null;
    });
    if (results.length > 0) return results;
    return list;
  }

  export default search;