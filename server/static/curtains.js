var client = new HttpClient();
var text = client.get('http://some/thing?with=arguments', function(response) {return response});
const stats = JSON.parse(text);
