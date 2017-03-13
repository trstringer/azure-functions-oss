module.exports = function (context, req) {
  context.log('... Entry point to HTTP trigger');

  if (req.query.message) {
    context.log('... message found in query string');
    res = {
      body: `Your message is "${req.query.message}"`
    };
  }
  else {
    context.log('... message not found in query string');
    res = {
      status: 400,
      body: 'Please pass a message in via the query string'
    };
  }

  context.done(null, res);
};
