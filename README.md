# Blockchain Snapshots
App for generating blockchain snapshots and provide them on the web page.

***Python web server*** programmed in ***Flask***.

***AJAX*** requests for refreshing the page data about snapshot file name in ***wget*** command.
```
pip3 install flask
pip3 install flask_cors
pip3 install waitress
```
### Conclusion
This is an illustration of a poor web server implemented using the Flask Python framework, as it obstructs all requests until one is finished, resulting in a blocking web server. 

This approach is unsuitable for large-scale applications and software that require a substantial volume of real-time request processing.

However, it may be appropriate for small-scale applications with fewer and smaller requests.
