 #!/bin/bash
app="nlp-flask"
docker build -t ${app} .
docker run -d -p 5000:5000 --name flask ${app}
exit 1
