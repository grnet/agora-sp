function shorten(str) {
  let short_str = '';
  short_str = strip(str);
  if(short_str.length > 40) {
    const trimmedString = short_str.substr(0, 40);
    short_str =  trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" "))) + '...';
  }
  return short_str;
}

function strip(html) {
  let txt = '';
  let tmp = document.createElement("DIV");
  tmp.innerHTML = html;
  txt = tmp.textContent || tmp.innerText || "";
  tmp.remove();
  return txt;
}

export {
  shorten,
  strip
};
