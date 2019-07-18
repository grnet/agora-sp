const {
  get,
} = Ember;

function shorten(str) {
  let short_str = '';

  short_str = strip(str);
  if(short_str.length > 40) {
    const trimmedString = short_str.substr(0, 40);

    short_str = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(' '))) + '...';
  }

  return short_str;
}

function strip(html) {
  let txt = '';
  let tmp = document.createElement('DIV');

  tmp.innerHTML = html;
  txt = tmp.textContent || tmp.innerText || '';
  tmp.remove();

  return txt;
}

function get_my_services(services, user_id) {

  return services.filter(function(service){
    let rejected = get(service, 'rejected_service_admins_ids').split(',');
    let pending = get(service, 'pending_service_admins_ids').split(',');
    let not = rejected.concat(pending);

    return !not.includes(user_id.toString());
  })
}

export {
  shorten,
  strip,
  get_my_services,
};
